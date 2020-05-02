"""filemanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from fm import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index.html"),
    path(r'view', views.view_detail, name='view_detail'),
<<<<<<< HEAD
    path(r'download',views.file_response,name='download'),
    path(r'email',views.email_view,name='email'),
    path(r'email_done',views.email_done,name='email_done'),
    path(r'screenshot',views.screenshot,name="screenshot"),
    path(r'camera',views.camera,name="camera"),
    path(r'settings',views.settings,name="settings"),
    path(r'settings_done',views.settings_done,name="settings_done"),
    path(r'smartfile_upload',views.upload_smartfile,name="smartfile"),
    path(r'shutdown',views.shutdown,name="shutdown"),
=======
    path(r'download',views.file_response,name='download')
>>>>>>> 14979eb57f97c05423aea52fa679fb9552adde4f
]
