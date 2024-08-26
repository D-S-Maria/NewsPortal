from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class ArticlesForm(forms.ModelForm):
    class Meta:
        text = forms.CharField(min_length=20)
        model = Post
        fields = [
            'title',
            'text',
            'author_post',
            'category'
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичным названию."
            )
        return cleaned_data


class NewsForm(forms.ModelForm):
    class Meta:
        text = forms.CharField(min_length=20)
        model = Post
        fields = [
            'title',
            'text',
            'author_post',
            'category'
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичным названию."
            )
        return cleaned_data
