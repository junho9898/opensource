# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth.models import User  #회원 관리해주는 기능 끌어오기 
from django.contrib import auth  
from django.template import loader            #회원 권한관리 기능 끌어오기
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate

 
def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))


