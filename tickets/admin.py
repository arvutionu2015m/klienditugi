from django.contrib import admin
from .models import Ticket
from .views import send_status_update
from .models import ResponseTemplate

@admin.register(ResponseTemplate)
class ResponseTemplateAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('subject', 'description')
    
    def save_model(self, request, obj, form, change):
        if change:  # Ainult kui staatust muudetakse
            previous_status = Ticket.objects.get(id=obj.id).status
            if previous_status != obj.status:
                send_status_update(obj)
        super().save_model(request, obj, form, change)

