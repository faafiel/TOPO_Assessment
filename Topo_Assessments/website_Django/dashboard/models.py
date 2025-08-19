import json

from django.db import models

# Create your models here.
import os
from django.conf import settings

class Industry(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    industry_Performance_List = models.JSONField(null=True, blank=True, default=list)
    company_List = models.JSONField(null=True, blank=True, default=list)
    # variables
   


    @classmethod
    def create_Industry (self, file):
        if self.pk is None:  # create if no exisiting pk
            name = "1"
            industry_performance_list = []
            company_list = []

            # nested for loop to extrat out data from json file and create sub-classes
            for industry_attribute in file:
                if industry_attribute == "name":
                    name = industry_attribute

                elif industry_attribute == 'industry_Performance_List':
                    industry_performance_list = industry_attribute
                    for quarter in industry_performance_list:
                        quarter_attribute_list = []
                        for quarter_attribute in quarter:
                            quarter_attribute_list.append(quarter_attribute)
                        tmp_industry_quarter = Industry_Quarters.create_industry_quarter(name,
                                                                                         quarter_attribute_list[0],
                                                                                         quarter_attribute_list[1],
                                                                                         quarter_attribute_list[2],
                                                                                         quarter_attribute_list[3],
                                                                                         quarter_attribute_list[4])
                        tmp_industry_quarter.save()

                elif industry_attribute == 'company_List':
                    company_list = industry_attribute 
                    


            tmp_company_obj = Industry(name= name,
                                      industry_performance_list = [],
                                      company_list = [])
            tmp_company_obj.save()
        # super().save(*args, **kwargs)  # Call the "real" save() method.


    def __str__(self):
        return self.name

# data_fields = models.JSONField(null=True, blank=True, default=list)

class Industry_Quarters(models.Model):
    year = models.IntegerField()
    quarter = models.CharField(max_length=4)
    revenue = models.IntegerField()
    memberships_Sold = models.IntegerField()
    avg_Duration_Mins = models.IntegerField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    @classmethod
    def create_industry_quarter(self, *args, **kwargs):
        if self.pk is None:  # create
            tmp_industry_quarter_obj = Industry_Quarters( *args, **kwargs)
            tmp_industry_quarter_obj.save()
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Company(models.Model):
    id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=256)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    company_Revenue = models.IntegerField()
    location  = models.CharField(max_length=50)
    # employee_List = models.JSONField(default=list)
    # q_Performance_List = ArrayField(models.foreignKey(q_Performance, on_delete=models.CASCADE))
    # client_List = models.JSONField(default=list)
    # a_Performance_List = models.JSONField(default=list)

    # @classmethod
    # def create_company (self, *args, **kwargs):
    #     if self.pk is None:  # create
    #         tmp_company_obj = Company(id=)
    #         tmp_company_obj.save()
    #     super().save(*args, **kwargs)  # Call the "real" save() method.

class Client(models.Model):
    date = models.CharField(max_length=40)
    membership_Id = models.CharField(max_length=5, primary_key=True)
    activity = models.CharField()
    revenue = models.IntegerField()
    duration_Min = models.IntegerField()
    location = models.CharField()
    comapany_id = models.ForeignKey(Company, on_delete=models.CASCADE)

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    cashmoney = models.IntegerField()
    hired_Date = models.CharField(max_length=20, null = True)
    comapany_id = models.ForeignKey(Company, on_delete=models.CASCADE)

class A_Performance(models.Model):
    year = models.IntegerField()
    total_Revenue = models.IntegerField()
    total_Membership_Field = models.IntegerField()
    top_Location = models.CharField()
    # quarters = models.JSONField(default=list)
    comapany_id = models.ForeignKey(Company, on_delete=models.CASCADE)   

class Q_Performance(models.Model):
    year = models.IntegerField()
    quarter = models.CharField(max_length=10)
    memebrships_Sold = models.IntegerField()
    avg_Duration_Min = models.IntegerField()
    revenue = models.IntegerField()
    profit_Margin = models.FloatField()
    a_performance = models.ForeignKey(A_Performance, on_delete=models.CASCADE) 

class Item(models.Model):
    name = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

#=====================================================================================
# Import and initialise entire db
file_path = os.path.join(settings.BASE_DIR, 'dashboard', 'unified_Data.json')
with open(file_path, 'r') as file:
    data = json.load(file)


tmp_industry = Industry.create_Industry(data)