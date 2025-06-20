from django.shortcuts import render,redirect
from django.http import HttpResponse
from CrudApp.models import Student,Register,Profile
from CrudApp.forms import Reg
from CrudApp.forms import RegistrationForm,ProfileForm
from django.contrib.auth import authenticate,login
from CrudProject import settings
from django.core.mail import send_mail


# Create your views here.
def create(request):
	if request.method=="POST":
		na=request.POST['uname']
		rnm=request.POST['rnm']
		age=request.POST['age']
		mb=request.POST['mbl']
		em=request.POST['em']
		add=request.POST['addr']
		Student.objects.create(name=na,rollno=rnm,age=age,mobile=mb,email=em,address=add)
		return redirect('/read')
	return render(request,'create.html',{})


def read(request):
	info=Student.objects.all()
	return render(request,'read.html',{"in":info})

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['uname']
		data.rollno=request.POST['rnm']
		data.age=request.POST['age']
		data.mobile=request.POST['mbl']
		data.email=request.POST['em']
		data.address=request.POST['addr']
		data.save()
		return redirect('/read')
	return render(request,'update.html',{'data':data})

def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/read')
	return render(request,'delete.html',{'info':ob})


def reg(request):
	if request.method=="POST":
		form=Reg(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>details saved sucessfully!!</h2>")
	form=Reg()
	return render(request,'reg.html',{'info':form})


def display(request):
	data=Register.objects.all()
	return render(request,'display.html',{'info':data})


def up(request,id):
  a=Register.objects.get(id=id)
  if request.method=="POST":
    u=Reg(request.POST,instance=a)
    if u.is_valid():
      u.save()
      return redirect('/display') 
  u=Reg(instance=a)
  return render(request,'up.html',{'u':u})
 

def de(request,id):
  d=Register.objects.get(id=id)
  if request.method=="POST":
    d.delete()
    return redirect('/display')
  return render(request,'del.html',{'d':d})

def register(request):
	form=RegistrationForm()
	if request.method=="POST":
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>Details are Submitted!!!</h2>")
	return render(request,'register.html',{'from':form})

def signin(request):
	if request.method=="POST":
		username=request.POST['uname']
		password=request.POST['pswd']
		u=authenticate(username=username,password=password)
		if u:
			login(request,u)
			return HttpResponse("<h2>Authenticated user!</h2>")
		else:
			return HttpResponse("<h2>invalid credintials</h2>")
	return render(request,'signin.html',{})


def profile(request):
	form=ProfileForm()
	if request.method=="POST":
		form=ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("<h2>Image is Uploaded sucessfully!</h2>")
	return render(request,'profile.html',{'f':form})

def data(request):
	d=Profile.objects.all()
	return render(request,'data.html',{'data':d})


def mail(request):
	if request.method=="POST":
		rcr=request.POST['em']
		sbj=request.POST['sub']
		m=request.POST['msg']
		t=settings.EMAIL_HOST_USER
		res=send_mail(sbj,m,t,[rcr])
		if res==1:
			return HttpResponse("<h1>mail sent</h1>")
		else:
			return HttpResponse("<h1>not sent</h1>")
	return render(request,'mail.html',{})
def home(request):
	return render(request,'home.html',{})