from django.shortcuts import render,HttpResponse,redirect
from django.http import request
# from blog.views import strategies
from exam.models import Exam,  Category
from course.models import Guider,Subject,Chapter,Quesions,Topic
from django.contrib import messages
from home.models import Contact, Newslatter_Subscriber
# Create your views here.
def exams(request):
       allexams = Exam.objects.all()
       allcats = Category.objects.all()
       print(allexams, allcats) 
       context = {
              'allexams': allexams,
               'allcats': allcats
       }
       return render(request,'Eduguider/exams.html', context)
def examdetails(request, slug_exam):
       exam = Exam.objects.filter(slug_exam=slug_exam).first() 
       allexam = Exam.objects.all()
       context = {'exam' : exam, 'allexam': allexam}
       return render(request, 'Eduguider/courses-details.html', context)
def notes(request, slug_exam):
       exam = Exam.objects.filter(slug_exam=slug_exam).first()
       subjects = Subject.objects.filter(exam_name=exam)                        
       context = {'exam':exam,
       }     
       return render(request, 'Eduguider/notesList.html', context)
def chapter(request, slug_chapter):
       chapter = Chapter.objects.get(slug_chapter=slug_chapter)    
       context = {'chapter':chapter} 
       return render(request, 'Eduguider/notes.html', context) 