from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(blank=True, null=True)
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
		
		# Modelul comentariilor devine inutil pentru ca folosim Disqus
		
#class Comment(models.Model):
#	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#	name = models.CharField(max_length=80)
#	email = models.EmailField()
#	body = models.TextField()
#	created = models.DateTimeField(auto_now_add=True)
#	updated = models.DateTimeField(auto_now=True)
#	active = models.BooleanField(default=True)
	
#	class Meta:
#		ordering = ('-created',)
		
#	def __str__(self):
#		return 'Comment by {} on {}'.format(self.name, self.post)