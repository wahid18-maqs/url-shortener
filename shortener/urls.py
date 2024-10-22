from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Points to the 'home' view
    path('<str:short_url>/', views.redirect_url, name='redirect'),  # Points to the 'redirect_url' view
    path('stats/', views.stats, name='stats'),  # Points to the 'stats' view
]
