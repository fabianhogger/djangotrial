from django.shortcuts import render
from django.http import HttpResponse
from .models import Furniture

# Create your views here.
def index(request):
	furns=Furniture.objects.all()
	return render(request,'index.html',{'furns':furns})
