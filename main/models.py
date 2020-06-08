from django.db import models
from django.db.models import Count
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
	title = models.CharField(max_length=50)
	contents = models.TextField()
	img = models.ImageField()
	dataCreat = models.DateTimeField()
	category = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class bokdae_SH(models.Model):
	build_y	= models.CharField(max_length=10)
	year	= models.CharField(max_length=20)
	month	= models.CharField(max_length=50)
	day	= models.CharField(max_length=10)
	dong	= models.CharField(max_length=10)
	bo_price= models.CharField(max_length=20)
	mo_price= models.CharField(max_length=10)
	size	= models.CharField(max_length=20)

	def __str__(self):
		return self.build_y

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
        build_y = models.CharField(max_length=10)
        offi_nm = models.CharField(max_length=100)
        size    = models.CharField(max_length=10)
        year    = models.CharField(max_length=10)
        month   = models.CharField(max_length=10)
        day     = models.CharField(max_length=10)
        dong    = models.CharField(max_length=10)
        bo_price= models.CharField(max_length=10)
        mo_price= models.CharField(max_length=10)
        floor   = models.CharField(max_length=10)

        def __str__(self):
                return self.build_y



class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

    def get_topic_count(self):
        return Topic.objects.filter(board=self).count()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def get_reply_count(self):
        return Post.objects.filter(topic=self).count()-1

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ("-last_updated",)


class Posts(models.Model):
    message = RichTextUploadingField()
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.message[:30]

    class Meta:
        ordering = ("-created_at",)
