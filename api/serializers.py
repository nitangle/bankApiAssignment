from django.contrib.auth.models import User


from rest_framework import serializers
from .models import BankDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # read_only_fields = '__all__'
        fields = ['id','username','email']

class BankInfoSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        validated_data.pop('ifsc_code', None)  # prevent myfield from being updated
        return super().update(instance, validated_data)

    class Meta:
        model = BankDetail
        # read_only_fields = ['ifsc_code']
        fields = '__all__'

