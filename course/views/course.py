from django.shortcuts import redirect, render,HttpResponse
from django.http import request
from course.models import Course,Video,UserCourse,Payment
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from EduGuider.settings import *
from time import time


import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
# Create your views here.

def courses(request):
       courses = Course.objects.filter(active=True)
       context = {
              'courses':courses
       }
       return render(request,'EduGuider/courses.html', context)
def course(request,slug):
    course = Course.objects.get(slug  = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number = 1 

    video = Video.objects.get(serial_number = serial_number , course = course)

    if (video.is_preview is False):

        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect(f"/courses/checkout/{course.slug}")
        
        
    context = {
        "course" : course , 
        "video" : video , 
        'videos':videos
    }
     
    return render(request,'Eduguider/course.html', context)
