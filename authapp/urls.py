from django.urls import path
from authapp.views import RegisterCreateView,  LoginCreateView, ProfileCreateView, LogoutUserView
app_name = 'authapp'

urlpatterns = [
    path('login/', LoginCreateView.as_view(), name="login"),
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/', ProfileCreateView.as_view(), name='profile'),
]
