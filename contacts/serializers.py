from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only 10 digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")

        return value

    def validate_email(self, value):
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Only Gmail address are allowed.")

        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Name must contain atleast 3 characters.")

        return value.title()

    def validate_company(self, value):
        if not value.strip():
            raise serializers.ValidationError("Company name cannot be empty.")

        return value.upper()

    def validate(self, attrs):
        if attrs["name"].lower() == attrs["company"].lower():
            raise serializers.ValidationError("Name and company cannot be same.")
        return attrs
