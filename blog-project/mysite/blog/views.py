from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetalView,CreateView,UpdateView,DeleteView)
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required # login_required decorator work for function based views only. so to use it for CBV we use mixins
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self): # allows to use django ORM when dealing with generic views. Refer django  documentation for more information
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetalView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView): # login_required decorator work for function based views only. so to use it for CBV we use mixins
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self): # allows to use django ORM when dealing with generic views. Refer django  documentation for more information
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
