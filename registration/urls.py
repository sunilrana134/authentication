from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    path('',views.home),
    path('dashboard/',views.dashboard),
    path('login/',LoginView.as_view(),name='login_url'),
    path('register/',views.register,name='register_url'),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name='logout'),
]