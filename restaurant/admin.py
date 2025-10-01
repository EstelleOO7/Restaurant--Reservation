from django.contrib import admin
from .models import Menu
from .models import Booking

# Register your models here.
admin.site.register(Menu)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'formatted_assigned_date')

    def formatted_assigned_date(self, obj):
        return obj.assigned_date.strftime("%d/%m/%y") if obj.assigned_date else "-"
    formatted_assigned_date.admin_order_field = 'assigned_date'
    formatted_assigned_date.short_description = 'Assigned Date'
 