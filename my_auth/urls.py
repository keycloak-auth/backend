from django.urls import path
from .views import keycloak_login

urlpatterns = [
    path('keycloak-login/', keycloak_login, name='keycloak-login'),
]