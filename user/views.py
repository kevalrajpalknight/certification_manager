from django.contrib.auth import get_user_model
from django.db.models import Q
from functools import reduce
from rest_framework import generics, filters

from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "name",
        "email",
        "phone",
        "address__local_address",
        "address__city",
        "certifications__certificate_name",
        "profession__profession",
    ]
    ordering_fields = [
        "name",
        "email",
        "phone",
        "address__local_address",
        "address__city",
        "certifications__certificate_name",
        "profession__profession",
    ]

    def get_queryset(self):
        queryset = (
            get_user_model()
            .objects.select_related("address")
            .prefetch_related("certifications", "profession")
            .exclude(is_superuser=True)
            .order_by("name")
        )
        return queryset
