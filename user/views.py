from django.contrib.auth import get_user_model
from rest_framework import generics, filters

from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = (
        get_user_model()
        .objects.select_related("address")
        .prefetch_related("certifications", "profession")
        .all().order_by('name')
    )
    serializer_class = UserSerializer
