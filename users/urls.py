from django.urls import path
from .views import Auth, User_Verification

app_name='user'
urlpatterns = [
    path('', Auth.as_view(), name="auth"),
    path('login', Auth.as_view(mode='login'), name='login_post'),
    path('register', Auth.as_view(mode='register'), name='register_post'),
    path('logout', Auth.as_view(mode='logout'), name='logout_post'),
    path('verification/<username>/<code>', User_Verification.as_view(), name='verification')
]