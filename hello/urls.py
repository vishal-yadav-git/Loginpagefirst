"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "CNG"
admin.site.site_title = "CNG 11"
admin.site.index_title = "Welcome to CNG"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('signup/', include('home.urls')),  # yourapp is the name of your app
    path('login/', include('home.urls')),
]

# Add media file handling in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)