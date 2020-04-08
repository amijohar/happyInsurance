import json                            
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.shortcuts import redirect,render
from rest_framework import status
#from . import serializers
from . import models
from . import forms

# Create your views here.


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            #serializer = serializers.UserSerializer(user)
            return HttpResponse('Login Successfull')
            #return JsonResponse(serializer.data)
        return HttpResponse(status=401)
    
    else:
        #form = forms.LoginForm()
        return render(request,'login.html')

def user_signup(request):

    if request.method == 'POST':
  
        if models.User.objects.filter(username=request.POST['username']).exists():
            return HttpResponse(status=403)
        else:
            form = forms.UserForm(request.POST)
            if form.is_valid:
                u = models.User(username=request.POST['username'])
                u.set_password(request.POST['password'])
                u.save()
                login(request, u)
                newUser = form.save(commit=False)
                newUser.user = u
                newUser.save()
                #serializer = serializers.UserSerializer(u)
                return HttpResponse(status=200)
    else:
        form = forms.UserForm()
        return render(request,'signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponse(status=200)