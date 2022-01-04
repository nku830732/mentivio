# from django.http import HttpResponse
# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render,HttpResponse
# from course.models import Course,Video,UserCourse,Payment
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.views.generic import ListView
# from EduGuider.settings import *
# from time import time



# import razorpay
# client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
# # Create your views here.

# def courses(request):
#        courses = Course.objects.filter(active=True)
#        context = {
#               'courses':courses
#        }
#        return render(request,'EduGuider/courses.html', context)
# def course(request,slug):
#     course = Course.objects.get(slug  = slug)
#     serial_number  = request.GET.get('lecture')
#     videos = course.video_set.all().order_by("serial_number")

#     if serial_number is None:
#         serial_number = 1 

#     video = Video.objects.get(serial_number = serial_number , course = course)

#     if (video.is_preview is False):

#         if request.user.is_authenticated is False:
#             return redirect("login")
#         else:
#             user = request.user
#             try:
#                 user_course = UserCourse.objects.get(user = user  , course = course)
#             except:
#                 return redirect("check-out" , slug=course.slug)
        
        
#     context = {
#         "course" : course , 
#         "video" : video , 
#         'videos':videos
#     }
     
#     return render(request,'Eduguider/course.html', context)
# # @login_required(login_url='/accounts/login')
# # def checkout(request , slug):
# #     course = Course.objects.get(slug  = slug)
# #     user = request.user
# #     action = request.GET.get('action')
# #     order = None
# #     payment = None
# #     error = None
# #     try:
# #         user_course = UserCourse.objects.get(user = user  , course = course)
# #         error = "You are Already Enrolled in this Course"
# #     except:
# #         pass
# #     amount=None
# #     if error is None : 
# #         amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
# #    # if ammount is zero dont create paymenty , only save emrollment obbect 
    
# #     if amount==0:
# #         userCourse = UserCourse(user = user , course = course)
# #         userCourse.save()
# #         return redirect('my-courses')   
# #                 # enroll direct
# #     if action == 'create_payment':

# #             currency = "INR"
# #             notes = {
# #                 "email" : user.email, 
# #                 "name" : f'{user.first_name} {user.last_name}'
# #             }
# #             reciept = f"nitish-{int(time())}"
# #             order = client.order.create(
# #                 {'receipt' :reciept , 
# #                 'notes' : notes , 
# #                 'amount' : amount ,
# #                 'currency' : currency
# #                 }
# #             )

# #             payment = Payment()
# #             payment.user  = user
# #             payment.course = course
# #             payment.order_id = order.get('id')
# #             payment.save()


    
# #     context = {
# #         "course" : course , 
# #         "order" : order, 
# #         "payment" : payment, 
# #         "user" : user , 
# #         "error" : error
# #     }
# #     print('order')
# #     return  render(request , template_name="Eduguider/course_checkout.html" , context=context )    
# # @method_decorator(csrf_exempt,name='dispatch')
# # def verifyPayment(request):
# #     if request.method == "POST":
# #         data = request.POST
# #         context = {}
# #         print(data)
# #         try:
# #             client.utility.verify_payment_signature(data)
# #             razorpay_order_id = data['razorpay_order_id']
# #             razorpay_payment_id = data['razorpay_payment_id']

# #             payment = Payment.objects.get(order_id = razorpay_order_id)
# #             payment.payment_id  = razorpay_payment_id
# #             payment.status =  True
# #             userCourse = UserCourse(user = payment.user , course = payment.course)
# #             userCourse.save()

# #             print("UserCourse" ,  userCourse.id)

# #             payment.user_course = userCourse
# #             payment.save()

# #             return redirect('my-courses')   

# #         except:
# #             return HttpResponse("Invalid Payment Details")