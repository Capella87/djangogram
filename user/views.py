from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets, status
from rest_framework import permissions
from .serializer import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile

# Create your views here.

@login_required
def user_profile(request):
    return render(request, 'user/profile.html')

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    lookup_field = "username"
    permission_classes = ( permissions.IsAuthenticated, )

    def get_queryset(self):
        return Profile.objects.all()


@api_view(['GET'])
def get_profile(request, username):
    prof = Profile.objects.get(username=username)
    prof_serializer = ProfileSerializer(prof, many=False)
    return Response(prof_serializer.data)
