from django.urls import path
from . import views

urlpatterns = [
    path('sendotp/', views.SendOTP.as_view(), name="send_otp"),
]
