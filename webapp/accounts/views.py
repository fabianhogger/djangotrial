from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
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
            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            return redirect('/accounts/registration')
        else:
            print("password doesn't match")
            return redirect('/accounts/registration')
    else:
        return render(request,'register.html')
