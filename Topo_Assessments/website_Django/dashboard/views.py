from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from dashboard.models import *

def index_page(request):
    return render(request, 'index.html')

def charts_page(request):
    template = loader.get_template('charts.html')
    return HttpResponse(template.render())

class ChartData(APIView):

    # Query out all required data from db and send it to frontend as a comprehensive package. The package is unpacked
    # at frontend

    def get(self, request, format = None):
        
        # Chart 1 ========================================================================================================
        quarter = Industry_Quarter.objects.values_list('quarter')
        year = Industry_Quarter.objects.values_list('year')
        revenue = Industry_Quarter.objects.values_list('revenue')

        c1_quarter_year = []
        counter = 0
        for each in quarter:

            tmp = str(year[counter]) + " " + str(quarter[counter])
            tmp = tmp.replace(",", "")
            tmp = tmp.replace("'", "")
            tmp = tmp.replace("(", "")
            tmp = tmp.replace(")", "")

            
            c1_quarter_year.append(tmp)
            counter += 1

        c1_revenue_list = []
        rev_counter = 0
        for each in revenue:
            tmp = str(revenue[rev_counter])
            tmp = tmp.replace(",", "")
            tmp = tmp.replace("'", "")
            tmp = tmp.replace("(", "")
            tmp = tmp.replace(")", "")
            c1_revenue_list.append(tmp)
            rev_counter += 1

        # Chart 2 ========================================================================================================
        client_list = Client.objects.filter(company_id=1)
        gym = []
        pool = []
        personal_training = []
        dance_class = []
        swimming_class = []
        yoga_class = []
        climbing_wall = []
        tennis_court = []

        for client in client_list:
            tmp = str(client.activity)
            tmp = tmp.replace(",", "")
            tmp = tmp.replace("'", "")
            tmp = tmp.replace("(", "")
            tmp = tmp.replace(")", "")
            if tmp == "Gym":    gym.append(client)
            elif tmp == "Pool": pool.append(client)
            elif tmp == "Personal Training": personal_training.append(client) 
            elif tmp == "Dance Class": dance_class.append(client)
            elif tmp == "Swimming Class": swimming_class.append(client)
            elif tmp == "Yoga Class": yoga_class.append(client)
            elif tmp == "Climbing Wall": climbing_wall.append(client)
            elif tmp == "Tennis Court": tennis_court.append(client)
            else:
                print("Not Captured")

        c2_chart_data = []
        c2_chart_data.append(len(gym))
        c2_chart_data.append(len(pool))
        c2_chart_data.append(len(personal_training))
        c2_chart_data.append(len(dance_class))
        c2_chart_data.append(len(swimming_class))
        c2_chart_data.append(len(yoga_class))
        c2_chart_data.append(len(climbing_wall))
        c2_chart_data.append(len(tennis_court))

        c2_labels = ["Gym", 
                    "Pool", 
                    "Personal training",
                    "Dance class", 
                    "Swimming class",
                    "Yoga class",
                    "Climbing wall",
                    "Tennis court"]

        data ={
                "c1_labels":c1_quarter_year,
                "c1_chart_label": "Industry Quarter Revenue",
                "c1_chart_data":c1_revenue_list,

                "c2_labels":c2_labels,
                "c2_chart_label":"Client activity breakdown by company",
                "c2_chart_data":c2_chart_data    
             }
        return Response(data)

def create_unified_data():

    # At this stage, all objects are constructed and stored in DB. So now we wil
    # nest together the objects instances. So that the data can be exported as a unfified structure. 
    # Start from bottom of pyramid
    # This function would be called upon server startup

    industry_query = Industry.objects.all()
    for industry in industry_query:

        company_query = Company.objects.filter(industry=industry.name)
        for company in company_query:

            clients_query = Client.objects.filter(company=company)
            clients_query_json = serializers.serialize('json', clients_query)
            company.client_list = clients_query_json

            employee_query = Employee.objects.filter(company=company)
            employee_query_json = serializers.serialize('json', employee_query)
            company.employee_list = employee_query_json

            annual_performance_query = A_Performance.objects.filter(company=company)    
            for annual_performance in annual_performance_query:

                annual_disto_query = A_Revenue_Distribution.objects.filter(a_performance=annual_performance)
                annual_disto_query_json = serializers.serialize('json', annual_disto_query)
                annual_performance.annual_rev_distribution_list = annual_disto_query_json

                q_performance_query = Q_Performance.objects.filter(a_performance=annual_performance)
                q_performance_query_json = serializers.serialize('json', q_performance_query)
                annual_performance.quarter_performance_list = q_performance_query_json

                annual_performance.save()

            annual_performance_query_json = serializers.serialize('json', annual_performance_query)
            company.annual_performance_list = annual_performance_query_json
            company.save()

        industry_quarter_query = Industry_Quarter.objects.filter(industry=industry.name)
        industry_quarter_query_json = serializers.serialize('json', industry_quarter_query)
        industry.industry_performance_list = industry_quarter_query_json

        company_query_json = serializers.serialize('json', company_query)
        industry.company_list = company_query_json

        industry.save()

#=====================================================================================

create_unified_data()