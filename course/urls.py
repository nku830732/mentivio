from . import views
from django.urls import path, include
from course.views import    verifyPayment , checkout,courses,course
urlpatterns = [  
    path('', courses, name="courses"),
    path('course_page/<str:slug>',course, name="course"),
    path('checkout/<str:slug>', checkout, name="checkout"),
]