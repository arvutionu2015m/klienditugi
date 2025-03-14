from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Ticket
import csv
from django.http import HttpResponse
from .forms import TicketForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from datetime import datetime
from django.core.paginator import Paginator
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logib kasutaja automaatselt sisse
            messages.success(request, "Konto on loodud! Tere tulemast.")
            return redirect('ticket_list')  # Suuname piletiloendi lehele
    else:
        form = UserCreationForm()

    return render(request, 'tickets/signup.html', {'form': form})

def export_tickets_pdf(request):
    tickets = Ticket.objects.filter(user=request.user)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tickets.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, height - 40, "Minu Klienditoe Piletid")

    y_position = height - 80
    p.setFont("Helvetica", 10)

    for ticket in tickets:
        p.drawString(50, y_position, f"Teema: {ticket.subject}")
        p.drawString(300, y_position, f"Staatus: {ticket.get_status_display()}")
        p.drawString(450, y_position, f"Prioriteet: {ticket.get_priority_display()}")
        y_position -= 20

        if y_position < 50:  # Kui leht saab täis, loo uus leht
            p.showPage()
            p.setFont("Helvetica", 10)
            y_position = height - 40

    p.showPage()
    p.save()
    return response

def export_tickets_csv(request):
    tickets = Ticket.objects.filter(user=request.user)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tickets.csv"'

    writer = csv.writer(response)
    writer.writerow(['Teema', 'Staatus', 'Prioriteet', 'Loodud', 'Viimati uuendatud'])

    for ticket in tickets:
        writer.writerow([ticket.subject, ticket.get_status_display(), ticket.get_priority_display(),
                         ticket.created_at.strftime('%d.%m.%Y %H:%M'),
                         ticket.updated_at.strftime('%d.%m.%Y %H:%M')])

    return response

def suggest_solution(ticket):
    solutions = {
        "Server error": "Palun proovige serveri taaskäivitust ja vaadake logifaile.",
        "Login issue": "Kontrollige, kas sisestatud e-post ja parool on õiged.",
        "Page not loading": "Proovige tühjendada brauseri vahemälu ja kontrollige võrguühendust.",
        "Bug report": "Palun saatke ekraanipilt ja logifailid, et saaksime probleemi uurida."
    }
    for key, solution in solutions.items():
        if key.lower() in ticket.subject.lower():
            return solution
    return "Teie probleem on registreeritud ja meie tiim vastab peagi!"

def send_status_update(ticket):
    subject = f"Teie pilet {ticket.subject} on uuendatud!"
    message = f"Tere {ticket.user.username},\n\n" \
              f"Teie pilet \"{ticket.subject}\" on uuendatud.\n\n" \
              f"Uus staatus: {ticket.get_status_display()}\n" \
              f"Prioriteet: {ticket.get_priority_display()}\n\n" \
              f"Vajadusel võtke meiega ühendust.\n\n" \
              f"Parimate soovidega,\nKlienditoe meeskond"

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [ticket.user.email])

def send_auto_reply(user_email, ticket):
    subject = f"Teie pilet on vastu võetud: {ticket.subject}"
    message = f"Tere {ticket.user.username},\n\n" \
              f"Teie klienditoe päring \"{ticket.subject}\" on edukalt registreeritud.\n" \
              f"Meie tiim vaatab selle üle ja vastab esimesel võimalusel.\n\n" \
              f"Pileti staatus: {ticket.get_status_display()}\n" \
              f"Prioriteet: {ticket.get_priority_display()}\n" \
              f"Loodud: {ticket.created_at}\n\n" \
              f"Tänan, et meiega ühendust võtsite!\n\n" \
              f"Parimate soovidega,\nKlienditoe meeskond"

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

def home(request):
    tickets = Ticket.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'tickets/home.html', {'tickets': tickets, 'year': datetime.now().year})

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)

    # Otsing
    query = request.GET.get('q')
    if query:
        tickets = tickets.filter(subject__icontains=query)

    # Filtreerimine staatuse järgi
    status_filter = request.GET.get('status')
    if status_filter:
        tickets = tickets.filter(status=status_filter)

    # Lehekülgede jagamine (10 piletit lehekülje kohta)
    paginator = Paginator(tickets, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tickets/ticket_list.html', {'tickets': page_obj})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    suggested_solution = suggest_solution(ticket)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket, 'suggested_solution': suggested_solution})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            
            # Automaatsed vastused
            send_auto_reply(request.user.email, ticket)
            
            messages.success(request, "Teie pilet on edukalt esitatud!")
            return redirect('ticket_list')
    else:
        form = TicketForm()

    return render(request, 'tickets/create_ticket.html', {'form': form})
