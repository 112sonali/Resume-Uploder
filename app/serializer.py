from rest_framework import serializers
from.models import *

class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'