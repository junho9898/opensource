import json, csv, os
import pandas as pd
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import StreamingHttpResponse
from .models import Post
from .models import list
from .models import bokdae_apt
from .models import bokdae_office

def index(request):
	postAll = Post.objects.all()
	return render(request, 'main/index.html', {'postAll':postAll})

def mapPage(request):
	return render(request, 'mapPage.html')

def bokdae_info(request):
#	foo = list.objects.all()
#	bar = {'dee':foo}
	search_key = request.GET.get('search_key',None)
	if search_key:
		foo = list.objects.filter(jw=search_key)
	else:
		foo = list.objects.all()
	bar = {'dee':foo}
	return render(request, 'bokdae_info.html', bar)

def bokdae_apt_list(request):
	search_key = request.GET.get('search_key',None)
	if search_key == '전세':
		aoo = bokdae_apt.objects.filter(mo_price = 0)
	elif search_key == '월세':
		aoo = bokdae_apt.objects.exclude(mo_price = 0)
	else:
		aoo = bokdae_apt.objects.all()
	aar = {'aee':aoo}
	return render(request, 'bokdae_apt.html', aar)

def bokdae_office_list(request):
        search_key = request.GET.get('search_key',None)
        if search_key:
                ooo = bokdae_office.objects.filter(jw=search_key)
        else:
                ooo = bokdae_office.objects.all()
        oar = {'oee':ooo}
        return render(request, 'bokdae_office.html', oar)
