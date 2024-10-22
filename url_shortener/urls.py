from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),
    path('<str:short_url>/stats/', views.stats, name='stats'),
]
