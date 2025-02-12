from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check-promotion/', views.check_promotion_eligibility, name='check_promotion_eligibility'),
    path('', views.check_promotion_eligibility, name='home'),  # Add this line for the root URL
]
