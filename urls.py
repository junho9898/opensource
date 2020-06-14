from django.urls import path
from blog import views
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name="index"),
    path("post/<int:pk>",views.PostDetailView.as_view(), name="Post"),
    path("post/create",views.Postcreate.as_view(), name="post_create"),
    path('register/',views.register),
    path('login/', views.login),
    path('member_del/', views.member_del,name='member_del'),
    path('mypage/', views.mypage,name="mypage" ),
    path('member_modify/', views.member_modify, name='member_modify'),
    path('change_pw/', views.change_pw, name='change_pw')
 ]