from rest_framework import serializers
from .models import Tasks

#Creating serializer for my model here.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tasks
        fields=('Date_Time','URL')