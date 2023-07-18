from rest_framework import serializers
from apps.business.models import Business


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'name', 'latitude', 'longitude']
