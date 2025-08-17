from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    cashmoney = models.IntegerField()
    hired_Date = models.CharField(max_length=20)

class Q_Performance(models.Model):
    year = models.IntegerField()
    quarter = models.CharField(max_length=10)
    memebrships_Sold = models.IntegerField()
    avg_Duration_Min = models.IntegerField()
    revenue = models.IntegerField()
    profit_Margin = models.FloatField()


class A_Performance(models.Model):
    year = models.IntegerField()
    total_Revenue = models.IntegerField()
    total_Membership_Field = models.IntegerField()
    top_Location = models.CharField()
    quarters = models.JSONField(default=list)

    
     
class Client(models.Model):
    date = models.CharField(max_length=40)
    membership_Id = models.CharField(max_length=5, primary_key=True)
    activity = models.CharField()
    revenue = models.IntegerField()
    duration_Min = models.IntegerField()
    location = models.CharField()


class Industry_Quarters(models.Model):
    year = models.IntegerField()
    quarter = models.CharField(max_length=4)
    revenue = models.IntegerField()
    memberships_Sold = models.IntegerField()
    avg_Duration_Mins = models.IntegerField()

class Company(models.Model):
    id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=256)
    industry = models.CharField(max_length=256)
    company_Revenue = models.IntegerField()
    location  = models.CharField(max_length=50)
    employee_List = models.JSONField(default=list)
    # q_Performance_List = ArrayField(models.foreignKey(q_Performance, on_delete=models.CASCADE))
    client_List = models.JSONField(default=list)
    a_Performance_List = models.JSONField(default=list)



class Industry(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    industry_Performance_List = models.JSONField(default=list)
    company_List = models.JSONField(default=list)

class Item(models.Model):
    name = models.CharField()
    created = models.DateTimeField(auto_now_add=True)