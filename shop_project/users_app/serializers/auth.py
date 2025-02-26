from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from users_app.models import User


class RegistrationUserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirmation",
            "role",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
        password_validation.validate_password(password=data.get("password"))
        if data["password"] != data["password_confirmation"]:
            raise serializers.ValidationError(
                {"password_confirmation": "Password doesn’t match"}
            )
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        del validated_data["password_confirmation"]
        user = User.objects.create(**validated_data)
        user.set_password(password)
        # user.is_active = False
        user.save()

        # send_confirmation_email.delay(user.pk)
        return user


class UserLoginOutputSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": "Incorrect email or password",
        "inactive": "This account is deactivated. Please contact the " "administrator if you wish to activate it",
    }

    def validate(self, attrs):
        attrs["email"] = attrs["email"].lower()
        data = super().validate(attrs)

        if self.user.is_active:
            data["user_id"] = self.user.id
            data["first_name"] = self.user.first_name
            data["last_name"] = self.user.last_name
            data["email"] = self.user.email
            data["user_role"] = self.user.role
            return data
        else:
            raise AuthenticationFailed("This account is deactivated")

#
# class CustomTokenRefreshSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super(CustomTokenRefreshSerializer, self).validate(attrs)
#         user = UserDAO.get_user_by_id(user_id)
#         return add_user_data(data, user)



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": ("Token is invalid or expired")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")
