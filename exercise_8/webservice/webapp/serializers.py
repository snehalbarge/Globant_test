from rest_framework import serializers
from .models import Employee_Details


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee_Details
        fields = '__all__'
