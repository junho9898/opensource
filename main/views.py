import json, csv, os
import pandas as pd
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, FormView, UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth

from .forms import TopicCreateForm, PostCreateForm
from .models import Post,bokdae_SH,bokdae_apt,bokdae_office,Board, Topic

#def index(request):
#	postAll = Post.objects.all()
#	return render(request, 'main/index.html', {'postAll':postAll})

def index(request):
    template = loader.get_template('main/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def mapPage(request):
	return render(request, 'mapPage.html')

def bokdae_info(request):
#	foo = list.objects.all()
#	bar = {'dee':foo}
	search_key = request.GET.get('search_key',None)
	if search_key:
		foo = bokdae_SH.objects.filter(jw=search_key)
	else:
		foo = bokdae_SH.objects.all()
	bar = {'dee':foo}
	return render(request, 'bokdae_info.html', bar)

def apt(request):
	return render(request, 'apt.html')

def bokdae_apt_list(request):
	search_key = request.GET.get('search_key',None)
	if search_key == '전세':
		aoo = bokdae_apt.objects.filter(mo_price = 0)
	elif search_key == '월세':
		aoo = bokdae_apt.objects.exclude(mo_price = 0)
	else:
		aoo = bokdae_apt.objects.all()
	aar = {'aee':aoo}
	return render(request, 'bokdae_apt.html', aar)

def bokdae_office_list(request):
        search_key = request.GET.get('search_key',None)
        if search_key:
                ooo = bokdae_office.objects.filter(jw=search_key)
        else:
                ooo = bokdae_office.objects.all()
        oar = {'oee':ooo}
        return render(request, 'bokdae_office.html', oar)






class BoardListView(ListView):
    template_name = "board_list.html"
    model = Board
    paginate_by = 8


class TopicListView(ListView):
    template_name = "topic_list.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["board"] = get_object_or_404(Board,pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        queryset = Topic.objects.filter(board__id=self.kwargs['pk'])
        return queryset


class TopicCreateView(LoginRequiredMixin, FormView):
    form_class = TopicCreateForm
    template_name = "new_topic.html"

    def form_valid(self, form):
        topic = form.cleaned_data.get('topic')
        message = form.cleaned_data.get('message')
        board = get_object_or_404(Board, pk=self.kwargs['pk'])
        new_topic = Topic.objects.create(
            subject=topic, board=board, starter=self.request.user)
        new_post = Post.objects.create(
            message=message, topic=new_topic, created_by=self.request.user)

        return redirect('TopicList', self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = get_object_or_404(Board, pk=self.kwargs['pk'])
        return context


class TopicPostsView(DetailView):
    model = Topic
    template_name = "topic_posts.html"

    def get_object(self):
        self.topic = get_object_or_404(
            Topic, board__pk=self.kwargs['pk'], pk=self.kwargs['topic_pk'])
        
        return self.topic

    def get_context_data(self, **kwargs):
        session_key = 'viewed_topic_{}'.format(self.topic.pk) # <-- here
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True           # <-- until here
        return super().get_context_data(**kwargs)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['message']
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'
    template_name = "update_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('TopicPosts', pk=post.topic.board.pk, topic_pk=post.topic.pk)


class PostReplyView(LoginRequiredMixin,CreateView):
    template_name = "reply_topic.html"
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = get_object_or_404(Topic, pk=self.kwargs['topic_pk'])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.topic = get_object_or_404(
            Topic, pk=self.kwargs['topic_pk'])
        instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('TopicPosts', kwargs={'pk': self.kwargs['pk'], 'topic_pk': self.kwargs['topic_pk']})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})



def index(request):
    template = loader.get_template('main/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))




def border_search(request):
    br = Post.objects.all() # 모든 Border 테이블의 모든 object들을 br에 저장하라

    b = request.GET.get('b','') # GET request의 인자중에 b 값이 있으면 가져오고, 없으면 빈 문자열 넣기

    if b: # b에 값이 들어있으면 true
        br = br.filter(title__icontains=b) # 의 title이 contains br의 title에 포함되어 있으면 br에 저장

    return render(request, 'border/border_search.html', { 'border_search':br , 'b':b})
    # br에는 Border 테이블에 title 이름이 'Singapore'인 데이터들이 들어있고,
    # b에는 내가 처음에 입력했던 'Singapore'가 들어있다.


def delete(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.delete()
    return redirect('/')
