from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from exam.models import Exam
from testseries.models import QuizCourse, Quiz, Quesition, Category, UserResponses, UserquizCourse, quizPayment, quizAttempt
from django.views.decorators.csrf import csrf_exempt
from EduGuider.settings import *
from time import time

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
# Create your views here.
def testserieses(request):
    allexams = QuizCourse.objects.all()
    allcats = Category.objects.all()
    context = {'allexams': allexams, 'allcats': allcats}
    return render(request, 'Eduguider/testserieses.html', context)
def testseries(request, slug):
    testseries = QuizCourse.objects.filter(slug=slug).first()
    tests = Quiz.objects.filter(quiz=testseries)
    context = {
        'testseries': testseries,
        'tests': tests
    }
    return render(request, 'Eduguider/testseries.html', context)
@login_required(login_url='/accounts/login')
def testseriescheckout(request, slug):
    course = QuizCourse.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    try:
        user_course = UserquizCourse.objects.get(user=user, course=course)
        error = "You are Already Enrolled in this Course"
    except:
        pass
    amount = None
    if error is None:
        amount = int(
            (course.price - (course.price * course.discount * 0.01)) * 100)
   # if ammount is zero dont create paymenty , only save emrollment obbect

    if amount == 0:
        userCourse = UserquizCourse(user=user, course=course)
        userCourse.save()
        return redirect('my-courses')
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

            payment = quizPayment()
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
    return render(request, "Eduguider/quizcoursecheckout.html", context)
@csrf_exempt
def verifyPaymenttest(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']
            payment = quizPayment.objects.get(order_id=razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.status = True
            userCourse = UserquizCourse(
                user=payment.user, course=payment.course)
            userCourse.save()

            print("UserquizCourse",  userCourse.id)

            payment.user_course = userCourse
            payment.save()
            messages.success(request, 'Payment Successful, You are enrolled')
            return redirect('home')

        except:
            return HttpResponse("Invalid Payment Details")
def tests(request):
    tests = Quiz.objects.filter()
    context = {
        
        'tests': tests
    }
    return render(request, "Eduguider/testlist.html", context)
@login_required
def test(request, slug):
    quiz = Quiz.objects.filter(slug=slug).first()
    user = request.user
    user_course = UserResponses.objects.filter(User=user, quiz=quiz).first()
    if user_course is None:
     if request.method == 'POST':
        questions = Quesition.objects.filter(quiz=quiz)
        user = request.user
        attempt = quizAttempt()
        attempt.user = user
        attempt.quiz = quiz
        attempt.save()
        for q in questions:
          que= request.POST.get(q.quesition)  
          print(request.POST.get(q.quesition))
          if que is not None:
            if q.correct ==  request.POST.get(q.quesition):
                sr_no = q.sr_no
                quiz = Quiz.objects.get(slug=slug)
                question = Quesition.objects.get(sr_no=sr_no)
                User = request.user
                answer = request.POST.get(q.quesition)
                status = True
                useranswer = UserResponses(quiz=quiz, question=question, User= User, answer=answer, status= status)
                useranswer.save()
            else:
                sr_no = q.sr_no
                quiz = Quiz.objects.get(slug=slug)
                question = Quesition.objects.get(sr_no=sr_no)
                User = request.user
                answer = request.POST.get(q.quesition)
                status = False
                useranswer = UserResponses(quiz=quiz, question=question, User= User, answer=answer, status= status)
                useranswer.save()
                
          else:
                sr_no = q.sr_no
                quiz = Quiz.objects.get(slug=slug)
                question = Quesition.objects.get(sr_no=sr_no)
                User = request.user
                status = False
                useranswer = UserResponses(quiz=quiz, question=question, User= User, status= status)
                useranswer.save()
        return redirect(f'/tests/solution/{quiz.slug}')     
        
     else:
      quiz = Quiz.objects.filter(slug=slug).first()
      
      context = {
        "quiz":quiz
      }
      return render(request, "Eduguider/testpage.html", context)
    else:
        # messages.error(request, "You message has been been successfully sent.We will reply as soon as possible.")
         return redirect(f'/tests/solution/{quiz.slug}')
@login_required
def solution(request, slug):
        quiz = Quiz.objects.get(slug=slug)
        user = request.user
        quesitions = Quesition.objects.filter(quiz=quiz)
        responses = UserResponses.objects.filter(quiz=quiz, User = user)
        score=0
        wrong=0
        correct=0
        total=0
        for response in responses:
          total +=1  
          if (response.status is True) :
            score+=10
            correct+=1
          else:
            wrong+=1
        
        percent = score/(total*10) *100
        context = {
            'quesitions':quesitions,
            'score':score,
            'percent': percent,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        print(context)
        # return redirect('tests')
        return render(request, "Eduguider/solution_page.html", context)        