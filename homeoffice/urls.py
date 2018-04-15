from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', login, {'template_name': 'authorization/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'authorization/logout.html'}, name='logout'),
]