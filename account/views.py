from django.shortcuts import render,redirect
from django.contrib.auth.models import User  #회원 관리해주는 기능 끌어오기 
from django.contrib import auth  
from django.http import HttpResponse
from django.template import loader            #회원 권한관리 기능 끌어오기
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
        	user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        	auth.login(request, user)
        	return redirect('/')
    return render(request, 'signup.html')

@csrf_exempt   
def login(request):
    if request.method == 'POST':
        #post 요청이 들어온다면
        username = request.POST.get('username', 'default value')
        password = request.POST.get('password', 'default value')
        user = auth.authenticate(request, username=username, password=password)
        #입력받은 아이디와 비밀번호가 데이터베이스에 존재하는지 확인.
        if user is not None: 
            #데이터 베이스에 회원정보가 존재한다면 로그인 시키고 home으로 돌아가기.
            auth.login(request, user)
            return redirect('/')
        else:
            #회원정보가 존재하지 않는다면, 에러인자와 함께 login 템플릿으로 돌아가기.
            return render(request, 'login.html', {'error': '아이디와 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'login.html')



 
def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))



def logout(request):
    auth.logout(request)
    #로그아웃 시키고 홈페이지로 보내기
    return redirect('/')