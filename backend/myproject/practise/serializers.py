from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Job

        
class JobSerializer(serializers.ModelSerializer):

    
    class Meta:
        model=Job
        fields="__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        
    def validate(self, data):
        start_date=data.get("start_date")
        end_date=data.get("end_date")

        if start_date and end_date:
            if start_date > end_date:
                raise serializers.ValidationError("End date cannot be earlier than Start date") 
        return data      

