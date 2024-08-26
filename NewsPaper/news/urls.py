from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostListSearch.as_view(), name='post_search'),
    path('create/', NewsCreated.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('create/', ArticlesCreated.as_view(), name='articles_create'),
    path('<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),
    path('<int:pk>/delete', ArticlesDelete.as_view(), name='articles_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),

]
