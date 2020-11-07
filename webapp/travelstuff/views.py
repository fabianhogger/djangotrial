from django.shortcuts import render
from django.http import HttpResponse
from .models import Furniture

# Create your views here.
def index(request):
	furn1=Furniture()
	furn1.name="KLemeni karekla"
	furn1.price=700
	furn1.img='p-1.jpg'
	furn2=Furniture()
	furn2.name="Kafe karekla sapia"
	furn2.price=300
	furn2.img='p-2.jpg'
	furn3=Furniture()
	furn3.name="Alvanikos komos"
	furn3.price=555
	furn3.img='p-3.jpg'
	furns=[furn1,furn2,furn3]
	return render(request,'index.html',{'furns':furns})
