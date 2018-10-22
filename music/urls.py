from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='music'),
    path('accordian', views.accordian, name='accordian'),

]
