from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
	title = models.CharField(max_length=255,null=True)
	pub_date = models.DateTimeField(null=True)
	image = models.ImageField(upload_to='images/')
	body = models.TextField(null=True)
	icon = models.ImageField(upload_to='images/')
	url = models.TextField(null=True)
	votes = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete = models.CASCADE)
	
	
	def __str__(self):
		return self.title
		
	def summary(self):
		return self.body[:100]