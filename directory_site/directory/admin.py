from django.contrib import admin
from .models import Category, Page

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_visits', 'number_of_likes')
    search_fields = ('name',)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)
