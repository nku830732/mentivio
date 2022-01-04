from . import views
from django.urls import path, include

urlpatterns = [
    path('<str:slug_exam>', views.examdetails, name="examdetails"),
    path('<str:slug_exam>/notes', views.notes, name="notes"),
    path('', views.exams, name="exams"),
    # path('quiz/', views.quiz, name="quiz"),
    path('notes/<str:slug_chapter>', views.chapter, name="chapter"),
]