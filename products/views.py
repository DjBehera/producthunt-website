from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone

# Create your views here.


def home(request):
	return render(request,'products/home.html')

@login_required	
def create(request):
	if request.method == "POST":
		print('HERE 1')
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
			print('here2')
			product = Products()
			product.title = request.POST['title']
			product.body = request.POST['body']
			product.url = request.POST['url']
			product.image = request.FILES['image']
			product.icon = request.FILES['icon']
			product.pub_date = timezone.datetime.now()
			product.votes = 1
			product.hunter = request.user
			product.save()
			return redirect('home')
		else:
			print('here3')
			return render(request,'products/create.html',{'error':'All fields Required'})
	else:
		print('here4')
		return render(request,'products/create.html')