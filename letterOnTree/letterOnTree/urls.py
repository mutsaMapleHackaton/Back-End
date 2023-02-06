from django.contrib import admin
from django.urls import path
from letterOnTreeApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('letterCreate', views.canvasToImage, name="letterCreate"),
    path('letterShow', views.filelist, name="letterShow")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)