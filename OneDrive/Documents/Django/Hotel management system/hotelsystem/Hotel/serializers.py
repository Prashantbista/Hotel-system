from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
        class Meta:
            model= Client
            fields = ["id","name","email","reservation_time","phone_number","table"]