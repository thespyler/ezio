from django.urls import path
from . import views
urlpatterns = [
    path('blog1/', views.blog1),
    path('blog2/', views.blog2),
    path('blog3/', views.blog3),
]
