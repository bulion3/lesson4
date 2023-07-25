from .views import index, top_sellers, lesson_4
from django.urls import path

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, 'top-sellers'),
    path('lesson_4/', lesson_4),
]