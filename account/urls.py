from django.urls import path
from django.conf.urls import url
from . import views
	
urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('mainapp/',views.index, name = 'index'),
        path('mainapp/accounts/login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'), 
]