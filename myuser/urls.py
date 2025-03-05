from django.urls import path, include
from .views import CustomLoginView, CustomLogoutView, home_view, CustomRegisterView

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]
