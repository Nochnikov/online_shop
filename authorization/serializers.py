from rest_framework import serializers

from authorization.models import User


class RegisSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_rewrite = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_rewrite']
        write_only_fields = ['password', 'password_rewrite']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']
