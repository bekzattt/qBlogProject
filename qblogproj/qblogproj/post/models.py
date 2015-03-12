from django.db import models
from django.utils import timezone


class Post(models.Model):
	
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	text = models.CharField(max_length=1000)
	pub_date = models.DateField(default=timezone.now)
	upd_date = models.DateField(default=timezone.now)
	is_public = models.BooleanField(default=False)
	def __unicode__(self):
		return unicode(self.title)+" / "+unicode(self.text)


class Comment(models.Model):

	author = models.CharField(max_length=200)
	text = models.CharField(max_length=1000)
	pub_date = models.DateField(auto_now_add=True)
	post = models.ForeignKey(Post)    
	def __unicode__(self):
		return unicode(self.author)+"/"+unicode(self.text)

    
