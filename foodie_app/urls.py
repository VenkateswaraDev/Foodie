from django.urls import path
from . import views
appName = 'foodie_app'
urlpatterns = [
    path('',views.index)
]
