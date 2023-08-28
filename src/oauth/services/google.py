from rest_framework.exceptions import AuthenticationFailed
from src.oauth import serializers
from google.oauth2 import id_token
from google.auth.transport import requests
from .base_auth import create_token
from src.oauth.models import AuthUser
from django.conf import settings


def check_google_auth(google_user: serializers.GoogleAuth) -> dict:
    try:
        id_token.verify_oauth2_token(
            google_user['token'], requests.Request(), settings.GOOGLE_CLIENT_ID)
    except ValueError:
        raise AuthenticationFailed(code=403, detail='bad token google')

    user, _ = AuthUser.objects.get_or_create(email=google_user.email)
    return create_token(user.id)
