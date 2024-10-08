from django.shortcuts import render,HttpResponse, redirect
from django.http import request
from exam.models import UserNew
from course.models import Chapter, Course, UserCourse, Topic, Guider
from home.models import Educator
from testseries.models import Quiz, QuizCourse, UserResponses,UserquizCourse
from dashboard.models import UserProfile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# @login_required
# def index(request):
#     return render(request,'EduGuider/index.html' )
@login_required(login_url='/accounts/login')
def dashboard(request):
    user= request.user
    usernews = UserNew.objects.filter(user=user)
    context = {
        'usernews':usernews,
        'user':user
    }
    return render(request, "Eduguider/admin/index.html", context)
@login_required(login_url='/accounts/login')
def profile(request):
    user= request.user
    if request.method=="POST":
        try:
            profile = UserProfile.objects.get(user=user)
            profile.delete()
        except:
            pass    
        profile = UserProfile()
        profile.first_name = request.POST['fname']
        profile.last_name = request.POST['lname']
        profile.Phone_No = request.POST['phone']
        profile.preparing_for = request.POST['preparingfor']
        profile.Email =  request.POST['email']
        profile.state =  request.POST['state']
        profile.city =  request.POST['city']
        profile.town_or_village =  request.POST['town']
        profile.user = request.user
        profile.save()
        messages.success(request,"Profile Updated")
        return redirect('dashboard')
    else:
        
        profile = UserProfile.objects.filter(user=user).first  
        context ={
           'profile': profile
        } 
        return render(request, "Eduguider/admin/user-profile.html", context)  
@login_required(login_url='/accounts/login')
def usercourses(request):
    user=request.user
    usercourses= UserCourse.objects.filter(user=user)
    recommendedcourses = Course.objects.all()
    context = {
        'usercourses' : usercourses,
        'recommendedcourses': recommendedcourses
    }   
    return render(request,'Eduguider/admin/courses.html', context)
@login_required(login_url='/accounts/login')
def usertestcourses(request):
    user= request.user
    usercourses = UserquizCourse.objects.filter(user=user)
    recommendedcourses=QuizCourse.objects.all()
    context = {
        'usercourses' : usercourses,
        'recommendedcourses': recommendedcourses
    } 
    return render(request,'Eduguider/admin/testserieses.html', context)
@login_required(login_url='/accounts/login')   
def userscores(request):
    user= request.user
    usertests = QuizCourse.objects.filter(user=user)
    context =  {
        'usertests' : usertests
    }
    return render(request,'Eduguider/admin/tests.html', context)
@login_required(login_url='/accounts/login')
def notes(request):
    user= request.user
    profile= UserProfile.objects.get(user=user)
    print(profile.preparing_for)
    notes = Chapter.objects.all()
    context= {
        'notes':notes
    }
    return render(request, "Eduguider/admin/notes.html", context)
@login_required(login_url='/accounts/login')
def guider(request):
    user= request.user
    profile= UserProfile.objects.get(user=user)
    guiders = Guider.objects.all()
    context={
        'guiders':guiders
    }
    return render(request, "Eduguider/admin/guider.html", context)
@login_required(login_url='/accounts/login')
def tests(request):
    user= request.user
    quizzes = Quiz.objects.all()
    recommendedcourses=QuizCourse.objects.all()

    context =  {
        'quizzes' : quizzes,
        'recommendedcourses': recommendedcourses,
    }
    return render(request,'Eduguider/admin/tests.html', context)
@login_required(login_url='/accounts/login')   
def userdoubt(request):
    return render(request,'Eduguider/admin/ask.html')
@login_required(login_url='/accounts/login')
def educatorhome(request):
    user= request.user
    educator=Educator.objects.get(user=user)
    context = {
        'educator': educator,
        'user':user
    }
    return render(request, "educatorDashboard/index.html", context)
    
# @login_required
# def educatorhome(request):
#     user= request.user
#     educator=Educator.objects.get(user=user)
#     context = {
#         'educator': educator,
#         'user':user
#     }
#     return render(request, "educatorDashboard/index.html", context)
