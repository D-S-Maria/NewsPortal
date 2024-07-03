from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostListSearch.as_view(), name='post_search')
]