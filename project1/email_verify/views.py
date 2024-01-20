from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import User

def email_form(request):
    if request.method == 'POST':
        global email
        email = request.POST.get('email')
        otp_code = "".join([str(random.randint(0, 9)) for i in range(6)])
        email_body = f'<h1>{otp_code}</h1>'
        send_mail('Expense App Email Verification Code', '', from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[email, ], html_message=email_body)
        user = User(email=email, otp=otp_code)
        user.save()
        return redirect('validate_otp')
    return render(request, 'email_verify/email_form.html')

def validate_otp(request):
    if request.method == 'POST':
        user_otp = request.POST['otp']
        # print(type(user_otp), type(user.otp), user_otp == user.otp)
        user = User.objects.get(email=email)
        if int(user.otp) == int(user_otp):
            return HttpResponse('<h1 style="color: green";>You are AUTHENTICATED!!!</h1>')
        else:
            return HttpResponse('<h1 style="color: red";>You are NOT AUTHENTICATED!!!</h1>')
    return render(request, 'email_verify/validate_otp.html')















#---------------------------------------------------------------------------------------------------------------

