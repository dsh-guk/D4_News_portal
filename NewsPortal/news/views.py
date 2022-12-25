from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from datetime import datetime

from .models import Author, Category, Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-pubDate']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['news_list'] = Post.objects.all()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    template_name = 'news/post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'news/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class SearchList(ListView):
    model = Post
    template_name = 'news/news_search.html'
    context_object_name = 'news'
    ordering = ['-pubDate']
    paginate_by = 10  # поставим постраничный вывод в 10 элементов

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['news_list'] = Post.objects.all()
        context['categories'] = Category.objects.all()
        return
