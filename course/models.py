from django.db import models
from ckeditor.fields import RichTextField
from exam.models import Exam,Category
from home.models import Educator
from django.contrib.auth.models import User

# Create your models here.
class Guider(models.Model):
    name = models.CharField(max_length=20,default="")
    Image = models.ImageField(upload_to="media/guider/",default="")
    Exam_qualified = models.ForeignKey(Exam, on_delete=models.CASCADE,default="")
    achievements = RichTextField(default="")
    slug_guider = models.CharField(max_length = 50,default="")
    time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['name', 'Exam_qualified']
    def __str__(self):
        return self.name +" qualifier of " + self.Exam_qualified.name
class Subject(models.Model):
       name = models.CharField(max_length=20,default="")
       exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, default="", blank=True)
       standard = models.IntegerField(null=True)
       slug_subject = models.CharField(max_length = 50,default="")
       class Meta:
        ordering = ['name','exam_name']
       def __str__(self):
        return self.name + self.exam_name.name       
class Chapter(models.Model):
    sr = models.IntegerField(default="")
    name = models.CharField(max_length=50,default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,default="")
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, default="")
    slug_chapter = models.CharField(max_length = 50,default="")
    designed_by = models.ForeignKey(Guider, on_delete=models.CASCADE,default="")
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name +" of " + self.subject.name + " for " + self.exam_name.name      
class Topic(models.Model):
    serial_no = models.AutoField
    name = models.CharField(max_length=200,default="")
    chapter_name = models.ForeignKey(Chapter, on_delete=models.CASCADE, default="")
    sub_name = models.ForeignKey(Subject, on_delete=models.CASCADE, default="")
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, default="", blank=True)
    waitage_in_exam = models.CharField(max_length=500,default="")
    notes = RichTextField(default="")
    quesitions_and_solutions = RichTextField(default="")
    
    slug_topic = models.CharField(max_length = 50,default="")
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name+" of " + self.sub_name.name + " for " + self.exam_name.name     
class Quesions(models.Model):
    marks = models.IntegerField(default="")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default="")
    exam_name = models.ForeignKey(Exam, on_delete=models.CASCADE, default="", blank=True)
    Quesion = RichTextField(default="")
    solution = RichTextField(default="")
    is_previousYearQuesition = models.BooleanField
    slug_quesition = models.CharField(max_length = 50,default="")
    class Meta:
        ordering = ['marks','topic']
    def __str__(self):
        return self.Quesion+" of " + self.topic.name + " for " + self.exam_name.name
class Course(models.Model):
    name = models.CharField(max_length = 50 , null = False)
    slug = models.CharField(max_length = 50 , null = False , unique = True)
    description = models.CharField(max_length = 200 , null = True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False , default = 0) 
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "media/courses/thumbnails/") 
    date = models.DateTimeField(auto_now_add= True) 
    resource = models.FileField(upload_to = "media/courses/notes/",blank=True)
    length = models.IntegerField(null=False)
    educator = models.ForeignKey(Educator,on_delete=models.CASCADE, blank=True)
    def __str__(self):
        return self.name
class Video(models.Model):
    title  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length = 100 , null=False)
    video = models.FileField(upload_to = "media/courses/videos/", blank=True)
    is_preview = models.BooleanField(default = False)
    description = models.TextField(max_length=100000, blank=True)
    def __str__(self):
        return self.title
class UserDoubt(models.Model):
    title = models.CharField(max_length=50, null=True)
    doubt_text = models.TextField(max_length=820, blank=True)
    doubt_image = models.ImageField(upload_to="media/doubts", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)        
class DoubtSolution(models.Model):
    solution = models.CharField(max_length=50000)
    date = models.DateTimeField(auto_now_add=True)
    doubt = models.ForeignKey(UserDoubt, on_delete=models.CASCADE)
    solved_by = models.ForeignKey(Guider, on_delete=models.CASCADE)
    is_free = models.BooleanField()
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
class CourseProperty(models.Model):
    description  = models.CharField(max_length = 100 , null = False)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)

    class Meta : 
        abstract = True
class CourseTag(CourseProperty):
    pass
class Prerequisite(CourseProperty):
    pass
class Learning(CourseProperty):
    pass
class UserCourse(models.Model):
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    course = models.ForeignKey(Course , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
class Payment(models.Model):
    order_id = models.CharField(max_length = 50 , null = False)
    payment_id = models.CharField(max_length = 50)
    user_course = models.ForeignKey(UserCourse , null = True , blank = True ,  on_delete=models.CASCADE)
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False) 
    amount = models.IntegerField(default=0)
class Materials(models.Model):
    title = models.CharField(max_length=50, default="")
    exam_name = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
    Description = models.TextField(max_length=500, blank=True)
    designed_by = models.ForeignKey(Guider, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
class MaterialSource(models.Model):
    material =  models.ForeignKey(Materials, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=80000, blank=True)
    extra_resource = models.FileField(upload_to="media/guider/resources")
class MatterialTag(models.Model):
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)