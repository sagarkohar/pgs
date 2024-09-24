"""
URL configuration for PGS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from PGS import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.first),
    path("index.html",views.first),
    path("about.html",views.about),
    path("class.html",views.classes),
    path("team.html",views.teachers),
    path("gallery.html",views.gallery),
    path("event.html",views.event),
    path("contact.html",views.contact),
    path("staff<int:id>",views.staff),
    path("feedback",views.feedback),
    path("register<int:id>",views.register),
    path("bookSeat",views.bookSeat),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
