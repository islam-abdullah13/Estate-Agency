from django.urls import path,include
from . import views

app_name='home'

urlpatterns = [
   path('', views.home, name='home'),
   path('estate', views.estate_list, name='estate'),
   path('<str:slug>', views.estate_detail, name='estate_detail'),
]