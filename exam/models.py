from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Exam(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to="media/explore/",default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    important_dates = RichTextField(default="")
    how_to_apply = RichTextField(default="")
    syllabus = RichTextField(default="")
    slug_exam = models.CharField(max_length = 50,default="")
    def __str__(self):
        return self.name
class Strategy(models.Model):
    exam_qualified = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text=" Name of exam qualifier")
    image = models.ImageField(upload_to="media/explore/",default="")
    short_description = RichTextField(default="")
    strategy = RichTextField(default="")
    slug_strategy = models.CharField(max_length = 50,default="")
    def __str__(self):
        return self.strategy + 'by' + self.name
class New(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = RichTextField()  
    image = models.ImageField(upload_to = "media/explore", default="")
    pub_date = models.DateField(default="now")
    def __str__(self):
        return self.title

class UserNew(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    news = models.ForeignKey(New, on_delete=models.CASCADE)        
    def __str__(self):
        return self.news.title
