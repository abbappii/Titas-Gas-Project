from rest_framework import serializers
from AuthenticationApp import models as auth_model


class AccountActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_model.User
        fields = ['id', 'email', 'full_name', 'profile_pic', 'is_active', 'active_request', 'is_suspended']
