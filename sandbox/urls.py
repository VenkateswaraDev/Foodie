from django.urls import path
from sandbox import views
urlpatterns = [
    path('',views.index),
]
