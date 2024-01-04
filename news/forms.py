from django import forms
from .models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'content', 'author', 'created_at', 'image', 'categories'
            ]
