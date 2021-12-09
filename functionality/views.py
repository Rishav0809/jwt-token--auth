from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .models import Details
from django.contrib.auth.decorators import login_required


def register(request):
    
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'register.html')
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                details=Details()
                details.user=request.POST['username']
                details.email=request.POST['email']
                details.address=request.POST.get('address',None)
                details.save()
                request.session.set_expiry(50000)
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'register.html',{'error':'This username has already been taken. Please try a new one.'})
            # except ValueError:
            #     return render(request,'register.html',{'error':'Some fields are empty.'})


        else:
            return render(request,'register.html',{'error':'The passwords did not match. Please try again.'})
    


def loginuser(request):
    
    if request.method=='GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        user=authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'error':'The credentials did not match.'})
        else:
            request.session.set_expiry(50000)
            login(request,user)
            return redirect('home')
    


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('loginuser')
    

def home(request):
    if request.user.is_authenticated:
        details=get_object_or_404(Details,user=request.user.username)
        print(details.user)
        return render(request,'index.html',{'details':details})
    else:
        return redirect('loginuser')



def deleteaddress(request):
    if request.method=='POST':
        details=get_object_or_404(Details,user=request.user.username)
        details.address="Add your address here"
        details.save()
    return redirect('home')

def deleteemail(request):
    if request.method=='POST':
        details=get_object_or_404(Details,user=request.user.username)
        details.email="Add your Email here"
        details.save()
    return redirect('home')  

def updatedetails(request):
    if request.method=='POST':
        # user=get_object_or_404(User, user=request.user.username)
        details=get_object_or_404(Details,user=request.user.username)
        # user.username=request.POST['user']
        # user.email=request.POST['email']
        # details.user=request.POST['user']
        details.email=request.POST['email']
        details.address=request.POST['address']
        # user.save()
        details.save()
    return redirect('home')


    