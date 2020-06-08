"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from main.views import index
import main.views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('mapPage/', main.views.mapPage, name='mapPage'),
    path('mapPage/apt', main.views.apt, name='apt'),
    path('mapPage/bda', main.views.bokdae_apt_list, name='bokdae_apt_list'),
    path('mapPage/bdo', main.views.bokdae_office_list, name='bokdae_office_list'),


    url(r'^accounts/',include('accounts.urls')),


    path('accounts/main/post/a/', main.views.BoardListView.as_view(), name="BoardList"),
    path('post/a/', main.views.BoardListView.as_view(), name="BoardList"),
    path('post/<int:pk>/', main.views.TopicListView.as_view(), name="TopicList"),
    path('post/<int:pk>/new/', main.views.TopicCreateView.as_view(), name="NewTopic"),
    path('post/<int:pk>/topics/<int:topic_pk>/',
         main.views.TopicPostsView.as_view(), name="TopicPosts"),
    path('post/<int:pk>/topics/<int:topic_pk>/edit/<int:post_pk>/',
         main.views.PostUpdateView.as_view(), name="PostUpdate"),
    path('post/<int:pk>/topics/<int:topic_pk>/reply/',
         main.views.PostReplyView.as_view(), name="PostReply"),
    path('post/a/main/', main.views.index, name = 'index'),
    path('post/search/', main.views.border_search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
