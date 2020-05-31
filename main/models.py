from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	contents = models.TextField()
	img = models.ImageField()
	dataCreat = models.DateTimeField()
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class list(models.Model):
	sigungu	= models.CharField(max_length=200)
	bunji	= models.CharField(max_length=20)
	doro	= models.CharField(max_length=50)
	area	= models.CharField(max_length=10)
	jw	= models.CharField(max_length=10)
	year	= models.CharField(max_length=20)
	day	= models.CharField(max_length=10)
	deposit	= models.CharField(max_length=20)
	rent	= models.CharField(max_length=10)

	def __str__(self):
		return self.sigungu

class bokdae_apt(models.Model):
	build_y	= models.CharField(max_length=20)
	year	= models.CharField(max_length=20)
	month	= models.CharField(max_length=20)
	day	= models.CharField(max_length=10)
	dong	= models.CharField(max_length=20)
	bo_price= models.CharField(max_length=10)
	mo_price= models.CharField(max_length=10)
	apt_nm	= models.CharField(max_length=200)
	size	= models.CharField(max_length=10)
	floor	= models.CharField(max_length=10)

	def __str__(self):
		return self.build_y

class bokdae_office(models.Model):
        sigungu = models.CharField(max_length=200)
        bunji   = models.CharField(max_length=20)
        danji   = models.CharField(max_length=20)
        jw      = models.CharField(max_length=10)
        area    = models.CharField(max_length=10)
        year    = models.CharField(max_length=10)
        day     = models.CharField(max_length=10)
        deposit = models.CharField(max_length=10)
        rent    = models.CharField(max_length=10)
        floor   = models.CharField(max_length=10)
        build   = models.CharField(max_length=10)
        doro    = models.CharField(max_length=20)

        def __str__(self):
                return self.sigungu

