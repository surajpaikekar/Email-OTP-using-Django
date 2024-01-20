from django.urls import path
from .views import email_form, validate_otp

urlpatterns = [
    path("email/", email_form, name='email_form'),
    path("otp/", validate_otp, name='validate_otp'),
]