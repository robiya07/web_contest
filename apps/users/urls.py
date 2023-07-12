from django.urls import path

from apps.users.views import registration_view, email_send_view, login_view, profile_view

app_name = 'users'

urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('email-send/', email_send_view, name='email-send'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
]
