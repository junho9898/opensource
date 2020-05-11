from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	contents = models.TextField()
	img = models.ImageField()
	dataCreat = models.DateTimeField()
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class bokdae(models.Model):
	sigungu	= models.CharField(max_length=200)
	bunji	= models.CharField(max_length=20)
	doro	= models.CharField(max_length=50)
	area	= models.CharField(max_length=10)
	year	= models.CharField(max_length=20)
	day	= models.CharField(max_length=10)
	deposit	= models.CharField(max_length=20)
	rent	= models.CharField(max_length=10)

	def __str__(self):
		return self.title
