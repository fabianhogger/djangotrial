from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method== 'POST':
        first_name=request.POST['First Name']
        last_name=request.POST['Last Name']
        email=request.POST['email']
        password1=request.POST['Password']
        password2=request.POST['Password2']
        username=request.POST['Username']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                messages.info(request,'username taken')
                return redirect('/accounts/registration')
            elif User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'email taken')
                return redirect('/accounts/registration')

            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                messages.info(request,'user taken')
                return redirect('/accounts/registration')
        else:
            print("password doesn't match")
            return redirect('/accounts/registration')
    else:
        return render(request,'register.html')
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password1=request.POST['Password']
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect("/travelstuff")
        else:
            messages.info("invalid credentials")
            return  redirect('accounts/login')
    return render(request,'login.html')
