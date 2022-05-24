from django.urls import path
from .views import login_view, logout_view, register_view

from django.contrib.auth import views as auth_views
from accounts.forms import PwdChangeForm

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('pwdchange/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/pwdchange.html', form_class=PwdChangeForm), name='pwdchange')
]