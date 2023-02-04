from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse #new

# Create your views here.



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Error has occured!')

    context={'form':form}
    return render(request,'app/register.html',context)

def loginRegisterUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form=UserCreationForm()
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.username=user.username.lower()
                user.save()
                login(request,user)
                return redirect('home')
        else:
            messages.error(request,'Error has occured!')
        context={'form':form}

        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Credential Invalid")
    return render(request,'app/login.html',context)

def home(request):
    return render(request, 'app/index.html')

# @login_required(login_url='loginRegister')
def logoutUser(request):
    logout(request)
    return redirect('login.html')


def my_list(request):
    return render(request, 'app/mylist.html')