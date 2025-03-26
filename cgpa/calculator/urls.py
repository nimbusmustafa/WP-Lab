from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_page, name='input'),  # Input page
    path('result/', views.result_page, name='result'),  # Result page
]
