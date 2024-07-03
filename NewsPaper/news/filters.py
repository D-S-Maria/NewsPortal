import django_filters
from django.forms import DateTimeInput
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, DateFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget, DateRangeWidget

from .models import Post, Category


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label='любой'
    )

    date = DateTimeFilter(
        field_name='date_created',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        )
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'type': ['icontains'],
        }
