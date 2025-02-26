from django.urls import path

from users_app.views.auth import UserLoginAPI, LogoutViewAPIView, CustomTokenRefreshView, RegistrationUserView

# roles types

# auth

urlpatterns = [
    path("signup/", RegistrationUserView.as_view(), name="signup"),
    path("login/", UserLoginAPI.as_view(), name="user-login"),
    path(
        "token_refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"
    ),
    path("logout/", LogoutViewAPIView.as_view(), name="user-logout"),
]

# users

#user profile
