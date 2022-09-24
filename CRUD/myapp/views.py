from genericpath import exists
from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
from myapp.models import Student
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
import json



# Create your views here.

def index(request):
    return render(request,'id/home.html',context={})


def login(request):
    return render(request,'id/login.html',context={})


def table(request):
    return render(request,'id/table.html',context={})    


def welcome(request):
    return render(request,'id/welcome.html',context={})

def form_data(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company']
        Email_name = request.POST['Email']
        phone_number = request.POST['Phone']
        password = make_password(request.POST['Password'])
        if Student.objects.filter(phone_number=phone_number).exists():
            messages.error(request,"phone number already exists")
            return redirect('/')    
 
        elif Student.objects.filter(Email_name=Email_name).exists():
            messages.error(request,"email already exists")
            return redirect('/')  

        else:
            Student.objects.create(first_name=first_name,
                                    last_name=last_name,company_name=company_name,
                                    Email_name=Email_name,phone_number=phone_number,password=password)
            return redirect('/login/')


        #creat login form
def Login_form(request):
            if request.method == 'POST':
                phone_number = request.POST['Phone']
                user_password = request.POST['Password']
                if Student.objects.filter(phone_number=phone_number).exists():
                    obj = Student.objects.get(phone_number=phone_number)
                    password = obj.password
                    if check_password(user_password,password):
                        return redirect('/welcome/')
                    else:
                        return HttpResponse('password incorrect')
            else:         
                    return HttpResponse('phone number is not registered')
    # create table data form
def data(request):
    persons = Student.objects.filter(is_active=True).order_by('id')

    return render(request,'id/table.html',context={
            'request' : request,
            'persons' : persons,
        })

    #create delete function

def delete_user(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        uid = json.loads(data)
        if Student.objects.filter(id=uid).exists():
            Student.objects.filter(id=uid).update(is_active=False)
            return JsonResponse({"staus": True, "message" : "user has been delete"})
        else:
            return JsonResponse({"staus": False, "message" : "user not exists"})
    else:
        return JsonResponse({"staus": False, "message" : "Method not allowed"})
#create edit update

def update_view(request, uid):
    res = Student.objects.get(id=uid)
    return render(request, 'id/update.html', context={

        'person': res,
    })

#use update data

def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company']
        Email_name = request.POST['Email']
        phone_number = request.POST['Phone']

        Student.objects.filter(id=uid).update(first_name=first_name,
                                    last_name=last_name,company_name=company_name,
                                    Email_name=Email_name,phone_number=phone_number)
        return redirect('/data/')

