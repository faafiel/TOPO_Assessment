from rest_framework import serializers
from dashboard.models import Item
from .models import *

class Item_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class Employee_Serializer(serializers.ModelSerializer):
    class meta:
        model = Employee
        field = (
            'id',
            'name',
            'role',
            'cashmoney',
            'hired_Date'
        )

class Client_Serializer(serializers.ModelSerializer):
    class meta:
        model = Client
        field = (
            'date',
            'membership_id',
            'activity',
            'revenue',
            'duration_Min'
        )

class A_Performance_Serializer(serializers.ModelSerializer):
    class meta:
        model = A_Performance
        field = (
            'year',
            'total_Revenue',
            'total_Membership_Field',
            'top_Location',
            'quarters'
        )