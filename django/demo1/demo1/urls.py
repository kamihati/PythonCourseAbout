"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as demo1_views

urlpatterns = [
    path("", demo1_views.index, name='index'),
    path("get_json/", demo1_views.get_json),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path("write/", demo1_views.write, name='write'),
    path("read/", demo1_views.read, name='read'),
    path('upload/', demo1_views.upload_file, name='upload_one'),
    path('upload_m/', demo1_views.upload_m, name="upload_m"),
    path("upload_success/", demo1_views.upload_success, name='upload_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

