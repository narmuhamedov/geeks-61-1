from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view),
    path('', views.auth_login_view, name='login'),
    path('logout/', views.auth_logout_view)
]

