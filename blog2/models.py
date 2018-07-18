from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse
from tinymce import HTMLField
#from PIL import Image

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = HTMLField('Text')
	#image = models.ImageField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def published(self):
		self.published_date = timezone.now()
		self.save()
		
		
	def __str__(self):
		return self.title
		
		