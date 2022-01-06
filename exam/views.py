from django.shortcuts import render,HttpResponse,redirect
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
       return render(request,'EduGuider/exams.html', context)
def examdetails(request, slug_exam):
       exam = Exam.objects.filter(slug_exam=slug_exam).first() 
       allexam = Exam.objects.all()
       context = {'exam' : exam, 'allexam': allexam}
       return render(request, 'EduGuider/courses-details.html', context)
def notes(request, slug_exam):
       if request.method=="POST":
                  name= request.POST['name']
                  email= request.POST['email']
                  phone= request.POST['phone']
                  content = request.POST['content']
                  print('name','email','phone','content')
                  if len(name)<2 or len(email)<8 or len(phone)<10 or len(content)<4:
                        messages.error(request,"Please fill the form correctly")
                  else:    
                    contact = Contact(name=name, email=email, phone=phone, content=content)
                    contact.save()
                    messages.success(request, "You message has been been successfully sent.We will reply as soon as possible.")
       allChaps=[]
       exam = Exam.objects.filter(slug_exam=slug_exam).first()
       subjects = Subject.objects.filter(exam_name=exam)
       # chapters1 = Chapter.objects.filter(exam_name=exam)

       for subject in subjects:
            chapters = Chapter.objects.filter(subject=subject)
            n = len(chapters)
            nChaps = n
            allChaps.append([chapters, range(1, nChaps), nChaps])                            
                
       context = {'exam':exam,'allChaps':allChaps}     
       return render(request, 'EduGuider/notesList.html', context)
def chapter(request, slug_chapter):
       allquesitions=[]
       chapter = Chapter.objects.filter(slug_chapter=slug_chapter).first()
       topics = Topic.objects.filter(chapter_name=chapter)
       for top in topics:
              quesition=Quesions.objects.filter()
              n = len(quesition)
              nQuesitions=n
              allquesitions.append([quesition, range(1, nQuesitions), nQuesitions])      
       context = {'chapter':chapter, 'topics':topics, 'allquesitions':allquesitions} 
       return render(request, 'EduGuider/notes.html', context) 
def quiz(request):
        return render(request, 'EduGuider/quiz.html')