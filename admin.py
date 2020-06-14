from django.contrib import admin
from blog.models import Category, Post ,Nickname
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin) :

    list_display = ('username', 'password')
class NicknameAdmin(admin.ModelAdmin) :
    list_display = ('nickname')

admin.site.register(User, UserAdmin)
admin.site.register(Nickname)

admin.site.register(Category)
admin.site.register(Post)

