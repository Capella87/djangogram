from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .serializer import ProfileSerializer
from .views import user_profile, ProfileViewSet
from rest_framework import routers

# https://stackoverflow.com/questions/59832790

user_router = routers.SimpleRouter()
user_router.register("user", ProfileViewSet, basename="user")

urlpatterns = [
]

urlpatterns += user_router.urls