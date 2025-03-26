# directory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.page_list, name='page_list'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_page/', views.add_page, name='add_page'),
]
