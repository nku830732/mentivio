from ast import Not
from unicodedata import category
from django.shortcuts import render,HttpResponse,redirect
from django.http import request
# from blog.views import strategies
from exam.models import Exam,  Category
from course.models import Guider,Subject,Chapter,Quesions,Topic
from django.contrib import messages
# Create your views here.
def exams(request):
       cat=request.GET.get('category')
       allcats = Category.objects.all()
       if cat is not None:
           ex=Category.objects.get(name= cat)   
           allexams=Exam.objects.filter(category=ex)
           context = {
              'allexams': allexams,
               'allcats': allcats,
               'ex':ex
       }
       else:
          allexams = Exam.objects.all()
          context = {
              'allexams': allexams,
               'allcats': allcats,
               
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