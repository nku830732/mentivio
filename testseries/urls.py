from . import views
from django.urls import path, include

urlpatterns = [
    # path('', views.tests, name='tests'),
    path('testserieses', views.testserieses, name='testserieses'),  
    path('testserieses/<str:slug>', views.testseries, name='testseries'),
    path('checkout/<str:slug>', views.testseriescheckout, name='testseriescheckout'),
    path('solution/<str:slug>', views.solution, name='solution'),
    path('attempt/<str:slug>', views.test, name='test'),
]