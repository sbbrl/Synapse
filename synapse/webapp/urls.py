from django.urls import path
from webapp import views
urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('explore/',views.explore),
]