from django.urls import path
from src.oauth.endpoint.auth_views import google_auth, google_login
from .endpoint import views


urlpatterns = [
    path('', google_login),
    path('google/', google_auth),
    path('me/', views.UserView.as_view({'GET': 'retrieve', 'PUT': 'update'}))
]
