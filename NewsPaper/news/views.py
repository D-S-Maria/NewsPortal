from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .filters import PostFilter
from .models import Post


# Create your views here.

class PostList(ListView):
    model = Post
    ordering = 'date_created'
    template_name = 'news.html'
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
