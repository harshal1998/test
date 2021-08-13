from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import test

# Create your views here.

def home(request):
	data=test.objects.all()
	if request.method=="POST":
		print("a")
		fname=request.POST['fname']
		lname=request.POST['lname']
		print(fname,lname)
		t = test(fname=fname,lname=lname)
		t.save()
		return HttpResponseRedirect("/")
	else:
		print("b")
		return render (request,'abc.html',context={"data":data})
	return render (request,'abc.html')




	