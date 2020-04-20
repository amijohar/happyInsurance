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
            return redirect('main:profile')
            #return JsonResponse(serializer.data)
        return HttpResponse(status=401)
    
    else:
        #form = forms.LoginForm()
        return render(request,'SignIn.html')

def user_signup(request):

    if request.method == 'POST':
  
        if models.User.objects.filter(username=request.POST['email']).exists():
            return HttpResponse(status=403)
        else:
            u = models.User(username=request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
            u.set_password(request.POST['password'])
            u.save()
            login(request, u)
            #serializer = serializers.UserSerializer(u)
            return redirect('main:profile')
    else:
        return render(request,'SignUp-form.html')

def user_logout(request):
    logout(request)
    return redirect('main:index')


def index(request):

    services = models.Services.objects.all()

    package = models.Packages.objects.all()

    packages = {}

    finalDict = []

    for o in services:
        if o.package_id not in packages:
            packages[o.package_id] = [o.service_name]
        else:
            packages[o.package_id].append(o.service_name)

    print(packages)


    return render(request,"index.html", {'data':packages, 'services':services, 'package':package})


def profile(request):

    if request.user.is_authenticated == False:

        return redirect('main:user_login')
    
    else:
        user = request.user

        services = models.Services.objects.all()

        package = models.Packages.objects.all()

        packages = {}

        finalDict = []

        for o in services:
            if o.package_id not in packages:
                packages[o.package_id] = [o.service_name]
            else:
                packages[o.package_id].append(o.service_name)

        print(packages)

        return render(request,"profile.html", {'user':user, 'data':packages, 'services':services, 'package':package })


def quote(request):


    if request.method == 'POST':

        print(request.POST) 
        print(request.FILES)

        user = request.user

        newUserInfo = models.Users(user=user, Contact_num = request.POST['contact'], Address = request.POST['address'], ID_proof = request.POST['id_proof'], Address_proof = request.POST['add_proof'])
        newUserInfo.save()

        newHistory = models.Financial_History(user_id = newUserInfo,monthly_income = request.POST['income'], monthly_expenses = request.POST['expenses'], bank_statement = request.POST['bank_statement'] )
        newHistory.save()

        diseases = request.POST.getlist('disease')

        for i in diseases:

            d = models.Diseases.objects.get(disease_id = i)
            newMedicalHistory = models.Medical_history(user_id = newUserInfo, disease_id = d)
            newMedicalHistory.save()

    
    else:
        # change services based on package selected
        package_type = request.GET['package']
        if package_type == 'Platinum':
            services = models.Services.objects.all()
        elif package_type == 'Premium':
            services = models.Services.objects.filter(package_id__package_type__in = ['Basic', 'Platinum'] )
        else:
            services = models.Services.objects.filter(package_id__package_type = package_type)
        diseases = models.Diseases.objects.filter(service_id__in = services)

        final_dict = {}
        for o in diseases:
            if o.service_id.service_name not in final_dict:
                final_dict[o.service_id.service_name] = [o]
            
            else:
                final_dict[o.service_id.service_name].append(o)
        print(final_dict)
        return render(request, "multistep.html", {'data':final_dict})


def purchase(request) :

    return render(request, "purchaseForm.html", {})

def myPlan(request) :

    return render(request, "myPlan.html",{})