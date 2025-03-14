from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/create/', views.create_ticket, name='create_ticket'),
    path('tickets/export/csv/', views.export_tickets_csv, name='export_tickets_csv'),
    path('tickets/export/pdf/', views.export_tickets_pdf, name='export_tickets_pdf'),
    path('login/', LoginView.as_view(template_name='tickets/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
