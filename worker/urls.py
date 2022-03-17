from django.urls import path, reverse
import django.contrib.auth.views as auth_views
from worker.views import register, email_verification

app_name = 'worker'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('reqister/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/auth/login/'), name='logout'),
    path('verification/', email_verification, name='verification'),
]