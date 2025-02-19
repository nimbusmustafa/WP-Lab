from django.contrib import admin
from django.urls import path
from book import views  # Import the views from the book app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page URL
    path('metadata/', views.metadata, name='metadata'),  # Metadata page URL
    path('reviews/', views.reviews, name='reviews'),  # Reviews page URL
    path('publisher/', views.publisher, name='publisher'),  # Publisher info page URL
]
