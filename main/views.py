from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Post
from .models import bokdae

def index(request):
	postAll = Post.objects.all()
	return render(request, 'main/index.html', {'postAll':postAll})

def mapPage(request):
	return render(request, 'mapPage.html')

def bokdae_info(request):
	infos = db.sqlite.objects.all()
	context = {'infos':infos}

	return render(request, 'bokdae_info.html', context)
