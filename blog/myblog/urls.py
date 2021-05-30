from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_pages),
    path('', views.index)
]
