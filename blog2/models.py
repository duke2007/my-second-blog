from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def published(self):
		self.published_date = timezone.now()
		self.save()
		
	#def get_absolute_url(self):
	#	return reverse('blog2:post_detail',
	#					args=[self.])
		
	def __str__(self):
		return self.title