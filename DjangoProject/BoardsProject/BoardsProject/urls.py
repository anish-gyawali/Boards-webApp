
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
]
