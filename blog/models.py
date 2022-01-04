from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BLANK_CHOICE_DASH
from exam.models import Exam
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Career_Oppotunitie(models.Model):
    name= models.CharField(max_length=50)
    exam_to_qualify= models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    desc = RichTextField()
    image = models.ImageField(upload_to="media/explore/",default="")
    slug = models.CharField(max_length=50)
    suggested_by = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name
class Career_Oppotunitie_Comment(models.Model):
    sr_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Career_Oppotunitie, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True) 
    comment = models.TextField(max_length=500) 
class Oppotunitie_Comment_Reply(models.Model):
    comment = models.ForeignKey(Career_Oppotunitie_Comment, on_delete=models.CASCADE, blank=True)
    time = models.DateTimeField(auto_now_add=True) 
    reply = models.TextField(max_length=500)         
class Career_OppotunitieTag(models.Model):
    title = models.CharField(max_length=50)
    career_oppotunities = models.ForeignKey(Career_Oppotunitie, on_delete=models.CASCADE)       
class Common_strategie(models.Model):
    title = models.CharField(max_length=500)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    description = RichTextField()  
    slug = models.CharField(max_length=50)
    suggested_by = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="media/explore/",default="")
    def __str__(self):
        return self.title
class strategyQuesition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Common_strategie, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True) 
    comment = models.TextField(max_length=500) 
    class Meta:    
        ordering = ['-time'] 
class strategyQuesitionReply(models.Model):
    quesition = models.ForeignKey(strategyQuesition, on_delete=models.CASCADE, blank=True)
    time = models.DateTimeField(auto_now_add=True) 
    reply = models.TextField(max_length=500)                
class Common_strategieTag(models.Model):
    title = models.CharField(max_length=50)
    common_strategies = models.ForeignKey(Common_strategie, on_delete=models.CASCADE)             
class blogAds(models.Model):
    title = models.CharField(max_length=500, default="")
    description = models.TextField(max_length=80000)
    time = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="media/explore/")
    slug = models.CharField(max_length=20, default="")
    class Meta:      
        ordering = ['-time'] 
class adsTag(models.Model):
    title = models.CharField(max_length=50, help_text='enter the title of post to embed it')
    ad = models.ForeignKey(blogAds, on_delete=DO_NOTHING)   