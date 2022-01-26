from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.utils.html import format_html
from dashboard.models import  UserProfile

# Register your models here.
class UserprofileModelAdmin(admin.ModelAdmin):
    list_display=["first_name","user","preparing_for","Email"]
   
admin.site.register(UserProfile, UserprofileModelAdmin)
