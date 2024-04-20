"""
Module containing URL patterns for the lessons app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonListView.as_view(), name="lessons-home"),
    path('lesson/<int:pk>/', views.LessonDetailView.as_view(), name="lessons-detail"),
    path('lesson/create/', views.LessonCreateView.as_view(), name="lessons-create"),
    path('lesson/<int:pk>/update/', views.LessonUpdateView.as_view(), name="lessons-update"),
    path('lesson/<int:pk>/delete/', views.LessonDeleteView.as_view(), name="lessons-delete"),
    path('about/', views.about, name="lessons-about"),
    path('contact/', views.contact, name="lessons-contact"),
    path('album/', views.album, name="lessons-album"),
]
