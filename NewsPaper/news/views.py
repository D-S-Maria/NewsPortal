from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import ArticlesForm, NewsForm
from .models import Post


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
class NewsCreated(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'NE'
        return super().form_valid(form)


class NewsEdit(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')


# все для статьи

class ArticlesCreated(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticlesEdit(UpdateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'AR'
        return super().form_valid(form)


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')
