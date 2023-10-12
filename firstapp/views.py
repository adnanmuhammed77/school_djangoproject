from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib import messages
 
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('registration_form')
        else:
            messages.info(request,'username or password is incorrect')
            return redirect('register')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username alredy taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request,'password not matching')
            return redirect('register')
         

    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def registration_form(request):
    if request.method=='POST':
        messages.info(request,'Well Done you have successfully registered' )
        return redirect('success')
       

    return render(request, 'registration_form.html')


def success(request):
    return render(request,'success.html')





