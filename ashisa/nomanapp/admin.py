from django.contrib import admin
from .models import Appointment
# Register your models here.
@admin.register(Appointment)
class Appointment  (admin.ModelAdmin):
    list_display = ('disease_category', 'name', 'email', 'date', 'time', 'phone')
    list_filter = ('disease_category', 'date')
    search_fields = ('disease_category', 'name', 'email', 'date', 'time', 'phone')
    ordering = ('date', 'time')