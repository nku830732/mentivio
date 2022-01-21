from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField(default="")
    email = models.CharField(max_length=500)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'message from ' + self.name
class Newslatter_Subscriber(models.Model):
    email_subscriber = models.CharField(max_length=100)
    def __str__(self):
        return "new subscriber " + self.email_subscriber
class Educator(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="media/educator/", blank=True)
    def __str__(self):
        return self.name
class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=True)
    Phone_No = models.PositiveIntegerField(null=False)
    Email = models.CharField(max_length=50,null=False)
    skills= models.CharField(max_length=50)
    resume = models.FileField(upload_to="media/applications")