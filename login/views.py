import math
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .backends import EmailPhoneAuthenticationBackend
from .models import EcomUser
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if math.isnan(float(request.POST['typecheck'])):
            user = EcomUser.objects.filter(email=username).exists()
            typecheck = True
        else:
            user = EcomUser.objects.filter(phone_number=username)
            typecheck = False
        if user:
            user_auth = EmailPhoneAuthenticationBackend.authenticate(typecheck,username=username,password=password)
            if user_auth is not None:
                request.session['user_session'] = user_auth.id
                return JsonResponse(
                    {'success':'True'},
                    safe = False
                )
            else:
                return JsonResponse(
                    {'success':'invalid'},
                    safe = False
                )
        else:
            return JsonResponse(
                {'success':'usernotfound'},
                safe = False
            )

    elif request.method == 'GET':
        return render(request,'login.html')