from django.contrib.auth.views import LoginView
from django.urls import path
from .views import get_cookie_view, set_cookie_view, set_session_view, get_session_view, logout_view, My_logout_view
from django.contrib.auth.views import LoginView

app_name = 'myauth'

urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name='myauth/login.html',
             redirect_authenticated_user=True,
         ),
         name='login',
         ),
    path("logout/", My_logout_view.as_view(), name="logout"),
    path("cookie/get/", get_cookie_view, name="cookie_get"),
    path("cookie/set/", set_cookie_view, name="cookie_set"),
    path("session/set/", set_session_view, name="session-set"),
    path("session/get/", get_session_view, name="session-get"),

]