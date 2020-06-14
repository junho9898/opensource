from django.shortcuts import render, redirect
from blog.models import Category, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Myuser, Nickname
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context= {
        "post_latest": post_latest
    }
    return render(req, "index.html", context=context)

class PostDetailView(generic.DetailView):
    model=Post

class Postcreate(LoginRequiredMixin, CreateView):
    model = Post
    fields=["title","title_image","content","category"]

def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get('username',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        res_data = {}
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else :
            user = User(username=username, password=make_password(password))
            user.save()
        return render(request, 'register.html', res_data) #register를 요청받으면 register.html 로 응답.

def login(request):
    response_data = {}

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)


        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else :
            myuser = Myuser.objects.get(username=login_username)
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                request.session['user'] = myuser.id
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html',response_data)

def home(request):
    user_id = request.session.get('user')
    if user_id:
        myuser_info = Myuser.objects.get(pk=user_id)  # pk : primary key
        return HttpResponse(myuser_info.username)  # 로그인을 했다면, username 출력

    return HttpResponse('로그인을 해주세요.')  # session에 user가 없다면, (로그인을 안했다면)

def logout(request):
    request.session.pop('user')
    return redirect('/')

def mypage(request):
	return render(request, 'mypage.html')

def member_modify(request) :
    if request.method == "POST":
        #id = request.user.id
        #user = User.objects.get(pk=id)
        user=request.user
        user.first_name = request.POST["first_name"]
        user.save()
        return redirect('/')
    return render(request, 'member_modify.html')

def register2(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'mypage.html')

    elif request.method == "POST":
        nickname = request.POST.get('nickname',None)   #딕셔너리형태


        res_data = {}
        if not (nickname) :
            res_data['error'] = "닉넥임을 입력해야 합니다."

        else :
            nickname = Nickname(nickname=nickname)
            nickname.save()
        return render(request, 'mypage.html', res_data) #register를 요청받으면 register.html 로 응답.

def member_del(request):
    if request.method == "POST":
        pw_del = request.POST["pw_del"]
        user= request.user
        if check_password(pw_del, user.password):
           user.delete()
           return redirect('blog/mypage')
    return render(request, 'member_del.html')

def change_pw(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                return redirect("/")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "change_pw.html",context)

