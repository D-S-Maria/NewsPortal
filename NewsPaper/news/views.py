from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import ArticlesForm, NewsForm
from .models import Post

from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.

class PostList(ListView):
    model = Post
    ordering = 'date_created'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10  # количество записей на странице

    # # Переопределяем функцию получения списка товаров
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context


class PostListSearch(ListView):
    model = Post
    ordering = 'date_created'
    template_name = 'news_search.html'
    context_object_name = 'posts'
    paginate_by = 10  # количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


# все для новости
class NewsCreated(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NE'
        return super().form_valid(form)


class NewsEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    model = Post

    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')


# все для статьи

class ArticlesCreated(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_articles',) # проверить!!!
    form_class = ArticlesForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticlesEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_articles',)
    form_class = ArticlesForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_articles',)
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')
