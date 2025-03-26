# mysite/urls.py

from django.contrib import admin  # This import was missing
from django.urls import path, include
from django.shortcuts import render, redirect

# Landing page view
def landing_page(request):
    return render(request, 'landing.html')

urlpatterns = [
    path('admin/', admin.site.urls),  # Now 'admin' is correctly imported
    path('users/', include('users.urls')),
    path('', landing_page, name='landing_page'),  # This serves the landing page at the root
]
