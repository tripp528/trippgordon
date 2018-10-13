from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='default'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('template/', views.template, name='template'),
]
