from rest_framework import serializers
from .models import Address, Profession, Certifications


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("local_address", "city")


class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = ("certificate_name", "duration")


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ("profession",)
