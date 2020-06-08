from django.urls import path
from django.conf.urls import url
from . import views
	
urlpatterns = [
    path('accounts/mainapp/post/a/',views.BoardListView.as_view(), name="BoardList"),
    path('post/a/', views.BoardListView.as_view(), name="BoardList"),
    path('post/<int:pk>/', views.TopicListView.as_view(), name="TopicList"),
    path('post/<int:pk>/new/', views.TopicCreateView.as_view(), name="NewTopic"),
    path('post/<int:pk>/topics/<int:topic_pk>/',
         views.TopicPostsView.as_view(), name="TopicPosts"),
    path('post/<int:pk>/topics/<int:topic_pk>/edit/<int:post_pk>/',
         views.PostUpdateView.as_view(), name="PostUpdate"),
    path('post/<int:pk>/topics/<int:topic_pk>/reply/',
         views.PostReplyView.as_view(), name="PostReply"),
    path('post/a/mainapp/',views.index, name = 'index'),
    path('post/search/', views.border_search, name='search'),
]