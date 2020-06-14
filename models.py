from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length = 50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post", args=[str(self.id)])

    def is_content_more300(self):
        return len(self.content) > 300

    def get_content_under300(self):
        return self.content[:300]

class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    username = models.CharField(max_length=64,verbose_name = '사용자명')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    #저장되는 시점의 시간을 자동으로 삽입해준다.

    def __str__(self):  # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'

class Myuser(models.Model):
    username= models.CharField(max_length = 64, verbose_name='사용자명')
    # verbose_name(장황한 이름?) 을 설정해주면 관리자페이지에서 username대신에 '사용자명'으로 뜬다.
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length = 64, verbose_name = '비밀번호')
    registered_time = models.DateTimeField(auto_now_add=True, verbose_name = '등록시간')
    #DateTimeField옵션 auto_now_add 현재시간 자동삽입.

    def __str__(self):  #admin페이지의
        return self.username
    class Meta :   #메타 클래스 _ 테이블을 이름 직접 설정할때. https://docs.djangoproject.com/en/3.0/ref/models/options/
        db_table = 'community_myuser'
        verbose_name = "사용자들(Meta)클래스"
        verbose_name_plural = "사용자들(Meta)클래스"


class Nickname(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    nickname = models.CharField(max_length=64,verbose_name = '닉네임')
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    #저장되는 시점의 시간을 자동으로 삽입해준다.

    def __str__(self):  # 이 함수 추가
        return self.nickname  # User object 대신 나타낼 문자

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_nickname'

