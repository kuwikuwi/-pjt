from django.urls import path, include
from .views import ProfileView 

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
]