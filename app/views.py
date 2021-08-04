from django.shortcuts import render
from django.http import HttpResponse
from .models import test

# Create your views here.

def a(request):
	if request.method == "POST":
		fname=request.POST['fname']
		lname=request.POST['lname']
		print(fname,lname)
		t = test(fname=fname,lname=lname)
		t.save()
		return render (request,'abc.html')
	return render (request,'abc.html')

	