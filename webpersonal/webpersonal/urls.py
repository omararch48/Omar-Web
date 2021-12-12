"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# Applications
from core import views as core_views
from projects import views as projects_views

# Settings for image visualization in Django admin
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name="home"),    
    path('projects/', projects_views.projects, name="projects"),
    path('blog/', core_views.blog, name="blog"),
    path('contact/', core_views.contact, name="contact"),    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)