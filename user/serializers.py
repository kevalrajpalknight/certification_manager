from django.contrib.auth import get_user_model
from rest_framework import serializers

from certification_manager.serializers import (
    AddressSerializer,
    CertificationsSerializer,
    ProfessionSerializer,
)


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    certifications = CertificationsSerializer(many=True)
    profession = ProfessionSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ("name", "email", "phone", "address", "certifications", "profession")
