from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
	if request.method == "POST":
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request,'account/signup.html',{'error':'Username is taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'account/signup.html',{'error':'Passwords do not match !!'})
	else:
		return render(request,'account/signup.html')

def login(request):
	if request.method == "POST":
		user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request,'account/login.html',{'error':'Incorrect Password or Username!!'})
	else:
		return render(request,'account/login.html')

def signout(request):
	if request.method == "POST":
		auth.logout(request)
		return redirect('home')
		