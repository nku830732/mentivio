from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db import models
from django.db.models.enums import Choices
from django.utils.html import format_html
from .models import Category, Exam, Strategy, New, UserNew

# Register your models here.
class userNewAdmin(admin.StackedInline):
    model = UserNew
class NewsAdmin(admin.ModelAdmin):
    inlines = [userNewAdmin]
    

admin.site.register(Category)
admin.site.register(Exam)
admin.site.register(Strategy)
admin.site.register(New,NewsAdmin)
admin.site.register(UserNew)