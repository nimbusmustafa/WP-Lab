from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_room, name='book_room'),
    path('rooms/', views.room_list, name='room_list'),
]
