from django_filters import FilterSet
from .models import Post


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'name': ['icontains'],
            'type': ['icontains'],
            'date_created': ['date__gt'],  # range
        }
