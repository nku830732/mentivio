from django import template
import math

from course.models import UserCourse , Course
from testseries.models import UserquizCourse ,quizAttempt
register = template.Library()

# 100 -> 10% --> mrp  - ( mrp * discount * 0.01 ) = selprice
@register.simple_tag
def cal_sellprice(price , discount):
    if discount == 0:
        return price
    sellprice = price
    sellprice = price - ( price * discount * 0.01 )
    return math.floor(sellprice)


@register.filter
def rupee(price):
    return f'₹{price}'
@register.simple_tag
def is_enrolled(request , course):
   
    user = None
    if not request.user.is_authenticated:
        return False
        # i you are enrolled in this course you can watch every video
    user = request.user
    try:
        user_course = UserCourse.objects.get(user = user  , course = course)
        return True
    except:
        return False
@register.simple_tag
def is_enrolled_test(request , course):
   
    user = None
    if not request.user.is_authenticated:
        return False
        # i you are enrooled in this course you can watch every video
    user = request.user
    try:
        user_course = UserquizCourse.objects.get(user = user  , course = course)
        return True
    except:
        return False
@register.simple_tag
def is_attempt(request , quiz):
   
    user = None
    if not request.user.is_authenticated:
        return False
        # i you are enrooled in this course you can watch every video
    user = request.user
    try:
        user_course = quizAttempt.objects.get(user = user  , quiz=quiz)
        return True
    except:
        return False
