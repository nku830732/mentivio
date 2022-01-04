from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import DateTimeField
from exam.models import Category, Exam
from home.models import  Educator
# Create your models here
class category(models.Model):
    quiz_type = models.CharField(max_length=50, help_text="mock test, concept booster, challenger,  topicwise, etc.")
class QuizCourse(models.Model):
    title = models.CharField(max_length=50, help_text="quiz type for exam,")
    exam  = models.ForeignKey(Exam, on_delete=DO_NOTHING, null=True)    
    description = models.TextField(max_length=5000, help_text="must include our features of our website")
    designed_by = models.ForeignKey(Educator, on_delete=DO_NOTHING)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False , default = 0) 
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "media/tests/thumbnails/") 
    date = models.DateTimeField(auto_now_add= True) 
    no_of_quizes = models.IntegerField(null=False)
    slug = models.CharField(max_length=50)
class Quiz(models.Model):
    type = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    quiz = models.ForeignKey(QuizCourse, on_delete=models.CASCADE, null=True, default="")
    name = models.CharField(max_length=50, default="")
    is_timed = models.BooleanField(default=True)
    is_preview = models.BooleanField(default=True)
    description = models.CharField(max_length=500)
    no_of_quesitions = models.IntegerField(default=0)
    slug = models.CharField(max_length=50)
class CourseProperty(models.Model):
    description  = models.CharField(max_length = 100 , null = False)
    quiz = models.ForeignKey(Quiz , null = False , on_delete=models.CASCADE)
    class Meta : 
        abstract = True
class quizTag(CourseProperty):
    pass    
class quizPrerequisite(CourseProperty):
    pass  
class Quesition(models.Model):
    quizcourse = models.ForeignKey(QuizCourse, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, default="")
    sr_no = models.AutoField(primary_key=True)
    quesition = models.TextField(max_length=808)
    option_1 = models.CharField(max_length=80)    
    option_2 = models.CharField(max_length=80)    
    option_3 = models.CharField(max_length=80)    
    option_4 = models.CharField(max_length=80)
    correct = models.CharField(max_length=88)
    solution = models.TextField(max_length=5000, default="", blank=True)
class quizAttempt(models.Model):
    quiz= models.ForeignKey(Quiz, on_delete= models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING)     
class UserResponses(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Quesition, on_delete=models.DO_NOTHING)
    User = models.ForeignKey(User, on_delete=DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=80, default="", blank=True)
    status = models.BooleanField(default=False)
class UserquizCourse(models.Model):
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    course = models.ForeignKey(QuizCourse , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.title}'
class quizPayment(models.Model):
    order_id = models.CharField(max_length = 50 , null = False)
    payment_id = models.CharField(max_length = 50)
    user_course = models.ForeignKey(UserquizCourse , null = True , blank = True ,  on_delete=models.CASCADE)
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    course = models.ForeignKey(QuizCourse , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False) 
    amount = models.IntegerField(default=0)