from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'',include('mainapp.urls')),
   url(r'^admin/',admin.site.urls),
   url(r'',include('post.urls')),
   url(r'^accounts/',include('accounts.urls')),
   path('ckeditor/', include('ckeditor_uploader.urls')),
]
