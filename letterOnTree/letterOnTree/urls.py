from django.contrib import admin
from django.urls import path
from letterOnTreeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('test', views.canvasToImage, name="test"),
]
