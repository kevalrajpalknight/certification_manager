from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = (
        get_user_model()
        .objects.select_related("address")
        .prefetch_related("certifications", "profession")
        .all()
    )
    serializer_class = UserSerializer
