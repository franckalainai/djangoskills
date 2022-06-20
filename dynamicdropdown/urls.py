from django.urls import path
from . import views

urlpatterns = [
    path('', views.dropdown, name='dropdown'),
    path('get-topics-ajax/', views.get_topics_ajax, name="get_topics_ajax"),
]