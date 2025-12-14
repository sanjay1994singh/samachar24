from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("news_category/<slug:slug>/", views.news_category, name="news_category"),
]
