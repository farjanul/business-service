import jwt
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.contrib.auth.models import AnonymousUser


class ServerUser(AnonymousUser):
    @property
    def is_authenticated(self):
        # Always return True. This is a way to tell if
        # the user has been authenticated in permissions
        return True


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if len(auth) == 1:
            raise exceptions.AuthenticationFailed(
                {"message": _("Invalid token header. No credentials provided.")}
            )

        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed(
                {"message": _("Invalid token header. Token string should not contain spaces.")}
            )

        try:
            jwt_token = auth[1].decode()
            header = jwt.get_unverified_header(jwt_token)
            claims = jwt.decode(
                jwt=jwt_token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=header["alg"]
            )
            user = ServerUser()
            return user, None

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed({'message': _("JWT Token Expired")})
        except jwt.InvalidSignatureError:
            raise exceptions.AuthenticationFailed({'message': _("Invalid sign key")})
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed({'message': _("Not enough segments in jwt token")})
        except Exception:
            raise exceptions.AuthenticationFailed({'message': _("Invalid JWT token")})

    def get_user(self, user_id):
        # Implement the logic to retrieve the user based on the user_id
        # Return the user object or None if not found
        pass
