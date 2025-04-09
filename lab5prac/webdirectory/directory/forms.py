from django import forms
from .models import Category, Page

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class PageForm(forms.ModelForm):
    class Meta:
        model=Page
        fields='__all__'
