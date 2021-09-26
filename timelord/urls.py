from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.home_add, name='home_add')
]

urlpatterns = format_suffix_patterns(urlpatterns)
