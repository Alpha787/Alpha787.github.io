from django.contrib import admin
from .models import Lead



class LeadNameAndMessage(admin.ModelAdmin):
    list_display = ['name', 'message', 'id']
    search_fields = ['name', 'message']


admin.site.register(Lead, LeadNameAndMessage)