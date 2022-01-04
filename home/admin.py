from django.contrib import admin
from .models import Contact , Newslatter_Subscriber, Educator

# Register your models here.
# Register your models here.
class contactA(admin.ModelAdmin):
    list_display = ('name','content','phone', 'email')
admin.site.register(Contact, contactA)
admin.site.register(Newslatter_Subscriber)
admin.site.register(Educator)