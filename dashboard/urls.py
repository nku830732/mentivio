
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('tests/', views.tests, name='tests'),
    path('usercourse/', views.usercourses, name = "usercourses"),
    path('usertestserieses/', views.usertestcourses, name = "usercourses"),
    # path('/', views., name=""),
    # path('Usertests/', views., name=""),
    # path('Userdoubts/', views., name=""),
    # path('Usernews/', views., name=""),
    path('guiders/', views.guider, name="guider"),
    path('usernotes/', views.notes, name="notes"),
    path('ask/', views.userdoubt, name="userdoubt"),
    # path('index/', views.index, name="index"),
]