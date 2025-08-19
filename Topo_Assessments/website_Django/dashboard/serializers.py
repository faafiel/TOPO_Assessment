from rest_framework import serializers
from dashboard.models import Item
from .models import *
import json

def importer ():
    with open('dashboard/fixtures/unified_data.json', 'r') as f:
        return json.load(f)

def json_slicer ():
    # This function will split up the unified data into seperate slices of data (list of objects) that can be deserialized
    # This is as the current unified structure is too deeply nested to deserialize properly

    dict = importer()
    print(dict)
    # json_data = '[{"model": "myapp.mymodel", "pk": 1, "fields": {"name": "Test", "value": 123}}]'

    # # Deserialize the JSON data
    # for obj in serializers.Serializer("json", dict):
    #     print(obj)
    #     # The deserialized object is a DeserializedObject instance
    #     # It wraps the model instance and related data
    #     instance = obj.object
    #     print(instance)
        # You can then save the instance to the database if needed
        # obj.save() 

# json_slicer()
# class Item_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'

# class Employee_Serializer(serializers.ModelSerializer):
#     class meta:
#         model = Employee
#         field = (
#             'id',
#             'name',
#             'role',
#             'cashmoney',
#             'hired_Date'
#         )

# class Client_Serializer(serializers.ModelSerializer):
#     class meta:
#         model = Client
#         field = (
#             'date',
#             'membership_id',
#             'activity',
#             'revenue',
#             'duration_Min'
#         )

# class A_Performance_Serializer(serializers.ModelSerializer):
#     class meta:
#         model = A_Performance
#         field = (
#             'year',
#             'total_Revenue',
#             'total_Membership_Field',
#             'top_Location',
#             'quarters'
#         )
#==========================================================================================================
# Serializing to json file
from datetime import datetime

# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()

# comment = Comment(email='leila@example.com', content='foo bar')

# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()

# serializer = CommentSerializer(comment)
# serializer.data
# {'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}

# from rest_framework.renderers import JSONRenderer

# json_file = JSONRenderer().render(serializer.data)
# json_file

#----------------------------------------------------------------------------------------------------------
class Industry:
     def __init__(self, name, industry_performance_list, company_list):
        self.name                       = name
        self.industry_performance_list  = industry_performance_list # 2D array of: [Year] BY [Quarter, Revenue, Memberships sold, AVG Duration(Minutes)]
        self.company_list               = company_list              # 1D array of Company objects

class IndustrySerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=256)
    industry_performance_list = serializers.JSONField(default=list)
    commpany_list = serializers.JSONField(default=list)

    def create(self, validated_data):
        return Industry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.industry_performance_list = validated_data.get('industry_performance_list', instance.industry_performance_list)
        instance.company_list = validated_data.get('created', instance.company_list)
        instance.save()
        return instance
     
#==========================================================================================================
# Deserialization: turn the json file into something python native
import io
from rest_framework.parsers import JSONParser

# stream = io.BytesIO('dashboard/fixtures/unified_data.json')
# data = JSONParser().parse(stream)

serializer = IndustrySerializer(data='dashboard/fixtures/unified_data.json')
serializer.is_valid()
# True
serializer.validated_data
# {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}


#==========================================================================================================
# Use that native python code to recreate models
# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Comment(**validated_data)

#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         return instance
    

#==========================================================================================================
# This commits the recreated model/class to the database

# def create(self, validated_data):
#     return Comment.objects.create(**validated_data)

# def update(self, instance, validated_data):
#     instance.email = validated_data.get('email', instance.email)
#     instance.content = validated_data.get('content', instance.content)
#     instance.created = validated_data.get('created', instance.created)
#     instance.save()
#     return instance

# Now when deserializing data, we can call .save() to return an object instance, based on the validated data.

# comment = serializer.save()