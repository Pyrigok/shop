from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_205_RESET_CONTENT
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenViewBase, TokenObtainPairView, TokenRefreshView

from users_app.models import User
from users_app.serializers.auth import UserLoginOutputSerializer, LogoutSerializer, RegistrationUserSerializer


class RegistrationUserView(generics.CreateAPIView):
    """User registration API View."""

    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationUserSerializer
    queryset = User.objects.all()


class UserLoginAPI(TokenObtainPairView):
    """API to login a user."""

    serializer_class = UserLoginOutputSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class LogoutViewAPIView(APIView):
    """API to log a user out."""

    @extend_schema(
        request=LogoutSerializer,
        responses={
            205: OpenApiResponse(response={"status": "ok", "details": "Logged out"}),
        },
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"status": "ok", "details": "Logged out"},
            status=HTTP_205_RESET_CONTENT,
        )
