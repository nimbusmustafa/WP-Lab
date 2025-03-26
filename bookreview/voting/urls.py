from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote_view, name='vote'),  # Voting page
    path('results/', views.result_view, name='results'),  # Results page
    path('reset/', views.reset_votes, name='reset_votes'),  # URL for resetting votes
]
