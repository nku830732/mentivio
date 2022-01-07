from django.shortcuts import render, redirect, HttpResponse
from django.http import request
from course.models import Course, Video, Payment, UserCourse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from EduGuider.settings import *
from time import time

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


@login_required(login_url='/accounts/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    try:
        user_course = UserCourse.objects.get(user=user, course=course)
        error = "You are Already Enrolled in this Course"
        return redirect
    except:
        pass
    amount = None
    if error is None:
        amount = int(
            (course.price - (course.price * course.discount * 0.01)) * 100)
   # if ammount is zero dont create paymenty , only save emrollment obbect
    if amount == 0:
        userCourse = UserCourse(user=user, course=course)
        userCourse.save()
        return redirect('/dashboard/usercourses')
        # enroll direct
    if action == 'create_payment':

        currency = "INR"
        notes = {
            "email": user.email,
            "name": f'{user.first_name} {user.last_name}'
        }
        reciept = f"eduguider-{int(time())}"
        order = client.order.create(
            {'receipt': reciept,
             'notes': notes,
             'amount': amount,
             'currency': currency
             }
        )

        payment = Payment()
        payment.user = user
        payment.course = course
        payment.order_id = order.get('id')
        payment.amount = amount
        payment.save()

    context = {
        "course": course,
        "order": order,
        "payment": payment,
        "user": user,
        "error": error
    }
    return render(request, template_name="Eduguider/course_checkout.html", context=context)


@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = Payment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True
            userCourse = UserCourse(user=payment.user, course=payment.course)
            userCourse.save()

            print("UserCourse",  userCourse.id)

            payment.user_course = userCourse
            payment.save()
            messages.success(request, 'Payment Successful, You are enrolled')
            return redirect('/dashboard/usercourses')

        except:
            return HttpResponse("Invalid Payment Details")
