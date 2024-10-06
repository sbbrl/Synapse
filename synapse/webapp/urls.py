from django.urls import path
from webapp import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
]