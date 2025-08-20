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
        # if self.pk is None:  # create if no exisiting pk
        name = "1"
        industry_performance_list = []
        company_list = []
        # nested for loop to extract out data from json file and create sub-classes
        for industry_attribute in file:
            if industry_attribute == "name":
                name = file[industry_attribute]
            
                tmp_industry_obj = Industry(name,
                                        industry_performance_list,
                                        company_list)
                tmp_industry_obj.save()

            
            elif industry_attribute == 'industry_Performance_List':

                custom_industry_quarter_id = 1
                industry_performance_list =  file[industry_attribute]
                for quarter in industry_performance_list:
                    quarter_attribute_list = []
                    for quarter_attribute in quarter:
                        quarter_attribute_list.append(quarter[quarter_attribute])

                    tmp_industry_quarter = Industry_Quarters.create_industry_quarter(custom_industry_quarter_id,
                                                                                     tmp_industry_obj,
                                                                                     quarter_attribute_list[0],
                                                                                    quarter_attribute_list[1],
                                                                                    quarter_attribute_list[2],
                                                                                    quarter_attribute_list[3],
                                                                                    quarter_attribute_list[4])
                    tmp_industry_quarter.save()
                    custom_industry_quarter_id += 1

            elif industry_attribute == 'company_List':
                company_list = file[industry_attribute]
                for company in company_list:
                    company_attribute_list = []
                    for company_attribute in company:
                        company_attribute_list.append(company[company_attribute])

                    tmp_company_obj = Company.create_company(company_attribute_list[0],
                                                             company_attribute_list[1],
                                                             tmp_industry_obj,
                                                             company_attribute_list[3],
                                                             company_attribute_list[4]) 
                    tmp_company_obj.save()

                    # At this stage, create employee, clients, perfromance classes, for current company in for loop
                    # 1: access employee list first. company_attribute_list[5] == employee_list
                    for employee in company_attribute_list[5]:
                        employee_attribute = []
                        for attribute in employee:
                            employee_attribute.append(employee[attribute])
                        tmp_employee_obj = Employee.create_Employee(employee_attribute[0],
                                                                    employee_attribute[1],
                                                                    employee_attribute[2],
                                                                    employee_attribute[3],
                                                                    employee_attribute[4],
                                                                    tmp_company_obj)
                        tmp_employee_obj.save()

                    # 2: access client list second. 
                    for client in company_attribute_list[7]:
                        client_attribute = []
                        for attribute in client:
                            client_attribute.append(client[attribute])
                        tmp_client_obj = Client.create_Client(client_attribute[0],
                                                            client_attribute[1],
                                                            client_attribute[2],
                                                            client_attribute[3],
                                                            client_attribute[4],
                                                            client_attribute[5],
                                                            tmp_company_obj
                                                            )
                        tmp_client_obj.save()

                    # 3: Create annual performance 
                    custom_a_performance_id = 1
                    for annual_performance in company_attribute_list[8]:
                        performance_attribute = []
                        for a_attribute in annual_performance:
                            performance_attribute.append(annual_performance[a_attribute])
                        tmp_a_performance_obj = A_Performance.create_annual_performance(custom_a_performance_id,
                                                                                        performance_attribute[0],
                                                                                        performance_attribute[1],
                                                                                        performance_attribute[2],
                                                                                        performance_attribute[3],
                                                                                        tmp_company_obj
                                                                                        
                                                                                        )
                        tmp_a_performance_obj.save()
                        custom_a_performance_id +=1

                        # 4: Create quarter performance
                        custom_q_performance_id = 1
                        for quarter in performance_attribute[4]:
                            quarter_performance_list = []
                            for q_attribute in  quarter:
                                quarter_performance_list.append(quarter[q_attribute])
                            tmp_q_performance_obj = Q_Performance.create_quarter_performance(custom_q_performance_id,
                                                                                             quarter_performance_list[0],
                                                                                             quarter_performance_list[1],
                                                                                             quarter_performance_list[2],
                                                                                             quarter_performance_list[3],
                                                                                             quarter_performance_list[4],
                                                                                             quarter_performance_list[5],
                                                                                             tmp_a_performance_obj)
                            tmp_q_performance_obj.save()
                            custom_a_performance_id =+ 1

                        custom_rev_id = 1
                        rev_distribution_list = []
                        for rev_attribute in performance_attribute[5]:
                            rev_distribution_list.append(performance_attribute[5][rev_attribute])

                        tmp_rev_distribution_obj = A_Revenue_Distribution.create_revenue_distribution(custom_rev_id,
                                                                                                    rev_distribution_list[0],
                                                                                                    rev_distribution_list[1],
                                                                                                    rev_distribution_list[2],
                                                                                                    rev_distribution_list[3],
                                                                                                    tmp_a_performance_obj)
                        tmp_rev_distribution_obj.save()
                        custom_rev_id =+ 1

class Industry_Quarters(models.Model):
    id = models.IntegerField(primary_key=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    year = models.IntegerField()
    quarter = models.CharField(max_length=4)
    revenue = models.IntegerField()
    memberships_Sold = models.IntegerField()
    avg_Duration_Mins = models.IntegerField()


    @classmethod
    def create_industry_quarter(self, id_, tmp_company_obj, year_, quarter_, revenue_, memberships_sold_, avg_Duration_Mins_):
        tmp_industry_quarter_obj = Industry_Quarters(id=id_,
                                                     industry=tmp_company_obj,
                                                     year=year_,
                                                     quarter=quarter_,
                                                     revenue=revenue_, 
                                                     memberships_Sold=memberships_sold_, 
                                                     avg_Duration_Mins=avg_Duration_Mins_)
        return tmp_industry_quarter_obj
    
       
class Company(models.Model):
    id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=256)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    company_revenue = models.FloatField()
    location  = models.CharField(max_length=50)

    @classmethod
    def create_company (self,id, name, industry, company_revenue, location):
        tmp_industry_quarter_obj = Company(id,
                                            name,
                                            industry,
                                            company_revenue,
                                            location)
        return tmp_industry_quarter_obj

class Client(models.Model):
    date = models.CharField(max_length=40)
    membership_id = models.CharField(max_length=5, primary_key=True)
    activity = models.CharField()
    revenue = models.FloatField()
    duration_min = models.IntegerField()
    location = models.CharField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 

    @classmethod
    def create_Client(self, date_, membership_id_, activity_, revenue_, duration_min_, location_, company_):
        tmp_client_obj = Client(date=date_,
                                membership_id=membership_id_,
                                activity=activity_,
                                revenue=revenue_,
                                duration_min=duration_min_,
                                location=location_,
                                company=company_
                                )
        return tmp_client_obj

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    cashmoney = models.IntegerField()
    hired_Date = models.CharField(max_length=20, null = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    @classmethod
    def create_Employee(self, employee_id, name, role, cashmoney, hired_date, company):
        tmp_employee_obj = Employee(employee_id,
                                    name,
                                    role,
                                    cashmoney,
                                    hired_date,
                                    company)
        return tmp_employee_obj

class A_Performance(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    total_revenue = models.IntegerField()
    total_membership_sold = models.IntegerField()
    top_location = models.CharField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 


    @classmethod
    def create_annual_performance (self, id_, year_, total_revenue_, total_membership_sold_, top_location_, company_):
        tmp_annual_performance_obj = A_Performance(id=id_,
                                                   year=year_, 
                                                   total_revenue=total_revenue_, 
                                                   total_membership_sold=total_membership_sold_,
                                                   top_location=top_location_,
                                                   company=company_
                                                   )
        return tmp_annual_performance_obj

class Q_Performance(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    quarter = models.CharField(max_length=10)
    membership_sold = models.IntegerField()
    avg_duration_min = models.IntegerField()
    revenue = models.IntegerField()
    profit_margin = models.FloatField(null = True)
    a_performance = models.ForeignKey(A_Performance, on_delete=models.CASCADE) 

    @classmethod
    def create_quarter_performance (self, id_, year_, quarter_, membership_sold_, avg_duration_min_, revenue_, profit_margin_, a_performance_):
        tmp_quarter_performance_obj = Q_Performance(id=id_,
                                                    year=year_, 
                                                  quarter=quarter_,
                                                  membership_sold=membership_sold_,
                                                  avg_duration_min=avg_duration_min_,
                                                  revenue=revenue_,
                                                  profit_margin=profit_margin_,
                                                  a_performance=a_performance_
                                                   )
        return tmp_quarter_performance_obj

class A_Revenue_Distribution(models.Model):
    id = models.IntegerField(primary_key=True)
    gym = models.IntegerField()
    pool = models.IntegerField()
    tennis_court = models.IntegerField()
    personal_training = models.IntegerField()
    a_performance = models.ForeignKey(A_Performance, on_delete=models.CASCADE) 

    @classmethod
    def create_revenue_distribution (self, id_, gym_, pool_, tennis_court_, personal_training_, a_performance_):
        a_revenue_distribution_obj = A_Revenue_Distribution(id=id_,
                                                            gym=gym_,
                                                            pool=pool_,
                                                            tennis_court=tennis_court_,
                                                            personal_training=personal_training_,
                                                            a_performance=a_performance_
                                                             )
        return a_revenue_distribution_obj


class Item(models.Model):
    name = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

#=====================================================================================
# Import and initialise entire db
file_path = os.path.join(settings.BASE_DIR, 'dashboard', 'unified_Data.json')
with open(file_path, 'r') as file:
    data = json.load(file)

tmp_industry = Industry.create_Industry(data)


#TODO

