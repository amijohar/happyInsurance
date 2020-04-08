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
            return redirect('main:index')
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
                return redirect('main:index')
    else:
        form = forms.UserForm()
        return render(request,'signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponse(status=200)


def index(request):

    if request.user.is_authenticated == False:

        return redirect('main:user_login')
    
    else:

        user = request.user.username

        services = models.Services.objects.all()

        packages = {}

        for o in services:
            if o.package_id.package_type not in packages:
                packages[o.package_id.package_type] = [o.service_name]
            else:
                packages[o.package_id.package_type].append(o.service_name)
        
        


        print(packages)


        return render(request,"index.html", {'user':user, 'data':packages})


def addMedicalHistory(request):

    if request.method == 'POST':

        a = 1
    
    else:

        return render(request, "medicalHistoryForm.html", {})


def addFinancialHistory(request):

    if request.method == 'POST':

        user = request.user.username
        search_user = models.User.objects.filter(username=user)
        main_user = models.Users.objects.filter(user=search_user[0])
        fileName = request.FILES['myFile'].name
        form = forms.FinancialHistoryForm(request.POST)
        if form.is_valid():
            newHistory = form.save(commit=False)
            newHistory.bank_statement = fileName
            newHistory.user_id = main_user[0]
            newHistory.save()

    
    else:
        form = forms.FinancialHistoryForm()
        return render(request, "financialHistoryForm.html", {'form':form})
