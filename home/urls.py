from . import views
from django.urls import path, include
from course.views import    verifyPayment
from testseries.views import verifyPaymenttest

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('faqs', views.faqs, name="faqs"),
    path("contact", views.contact, name='contact'),
    path('membership', views.membership, name="membership"),
    path('accounts/login', views.handleLogin, name="login"),
    path('accounts/signup', views.handleSignup, name="register"),
    path('forgetpass', views.forgetpass, name="forgetpass"),
    path('success/url/', views.success, name="success"),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('verify_paymenttest', verifyPaymenttest , name = 'verify_paymenttest'),
]