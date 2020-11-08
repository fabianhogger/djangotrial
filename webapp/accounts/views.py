from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method== 'POST':
        first_name=request.['First Name']
        last_name=request.['Last Name']
        email=request.['email']
        password=request.['Password']
        password2=request.['Password2']
        username=request.['Username']
    else:
        return render(request,'register.html')
