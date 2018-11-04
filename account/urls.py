from django.urls import path
from . import views

urlpatterns = [
	path('signup/',views.signup,name='signup'),
	path('signout/',views.signout,name='signout'),
	path('login/',views.login,name='login'),
]