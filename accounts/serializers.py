from rest_framework import serializers

from accounts.models import Organization
from accounts.models import User


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
        read_only_fields = ("id",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = (
            "id",
            "is_superuser",
            "is_staff",
            "last_login",
            "date_joined",
            "last_modified",
            "created",
            "groups",
            "user_permissions",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
