from rest_framework.permissions import BasePermission

from users_app.constants import UserRoles


class Permissions:
    class ClientPermission(BasePermission):
        def has_permission(self, request, view):
            user = getattr(request, "user", None)
            return bool(
                user and user.is_authenticated and user.role == UserRoles.CLIENT
            )


    class SellerPermission(BasePermission):
        def has_permission(self, request, view):
            user = getattr(request, "user", None)
            return bool(
                user and user.is_authenticated and user.role == UserRoles.SELLER
            )
 