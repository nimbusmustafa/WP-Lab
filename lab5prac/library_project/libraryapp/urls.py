from django.urls import path
from . import views

urlpatterns=[
    path('', views.dashboard, name='dashboard'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-borrower/', views.add_borrower, name='add_borrower'),
    path('issue-book/', views.issue_book, name='issue_book'),

]