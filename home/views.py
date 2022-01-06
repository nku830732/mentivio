from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Contact, Newslatter_Subscriber
# Create your views here.
def home(request):
       
    return render(request,'EduGuider/solution_page.html' )
def about(request):
       
    return render(request,'EduGuider/about-1.html' )
def faqs(request):
    return render(request,'EduGuider/faq-1.html' )
def contact(request):
    
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

       
    return render(request, 'EduGuider/contact-1.html') 
def membership(request):
       return render(request,'EduGuider/membership.html')
# def login(request):
       
#        return render(request,'EduGuider/login.html')
# def register(request):
       
#        return render(request,'EduGuider/register.html')
def forgetpass(request):
       
       return render(request,'EduGuider/forget-password.html')
def handleSignup(request):       
    if request.method == "POST":
        username = request.POST['username']
        First_name = request.POST['fname']
        Last_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and number")
            return redirect('home')
        if pass1!= pass2:
            messages.error(request,  "password do not match")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=First_name
        myuser.last_name = Last_name
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        return redirect("login")
    else:
       return render(request,'account/signup.html')
          
          
def handleLogin(request):  
  action = request.GET.get('next')  
  print(action)  
  if request.user.is_authenticated is False:              
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        action = request.GET.get('next')  
        print(action)  
        if user is not None:
            login(request, user)
            messages.success(request,"successfully logged in")
            return redirect('/dashboard/profile')
        else:
            messages.error(request,'try again')
    return render(request,'account/login.html') 
  else:
    return redirect('/dashboard/profile')   
            
            

       

def success(request): 
    return redirect('home')
