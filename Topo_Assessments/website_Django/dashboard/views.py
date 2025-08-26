from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, FileResponse
from django.template import RequestContext

from django.core import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from dashboard.models import *
from pathlib import Path

def index_page(request):
    return render(request, 'index.html')

def charts_page(request):
    template = loader.get_template('charts.html')
    return HttpResponse(template.render())

class ChartData(APIView):

    def get(self, request, format = None):
        
        # Chart 1 ========================================================================================================
        quarter = Industry_Quarters.objects.values_list('quarter')
        year = Industry_Quarters.objects.values_list('year')
        revenue = Industry_Quarters.objects.values_list('revenue')

        c1_quarter_year = []
        counter = 0
        for each in quarter:

            tmp = str(year[counter]) + " " + str(quarter[counter])
            tmp = tmp.replace(",", "")
            tmp = tmp.replace("'", "")
            tmp =  tmp.replace("(", "")
            tmp =  tmp.replace(")", "")

            
            c1_quarter_year.append(tmp)
            counter += 1

        c1_revenue_list = []
        rev_counter = 0
        for each in revenue:
            tmp = str(revenue[rev_counter])
            tmp = tmp.replace(",", "")
            tmp = tmp.replace("'", "")
            tmp =  tmp.replace("(", "")
            tmp =  tmp.replace(")", "")
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
            tmp =  tmp.replace("(", "")
            tmp =  tmp.replace(")", "")
            if tmp == "Gym":
                gym.append(client)
            elif tmp == "Pool":
                pool.append(client)
            elif tmp == "Personal Training":
                personal_training.append(client) 
            elif tmp == "Dance Class":
                dance_class.append(client)
            elif tmp == "Swimming Class":
                swimming_class.append(client)
            elif tmp == "Yoga Class":
                yoga_class.append(client)
            elif tmp == "Climbing Wall":
                climbing_wall.append(client)
            elif tmp == "Tennis Court":
                tennis_court.append(client)
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


        c1_chart_label = "Industry Quarter Revenue"
        c2_chart_label = "Client activity breakdown by company"
        data ={
                "c1_labels":c1_quarter_year,
                "c1_chart_label":c1_chart_label,
                "c1_chart_data":c1_revenue_list,

                "c2_labels":c2_labels,
                "c2_chart_label":c2_chart_label,
                "c2_chart_data":c2_chart_data    
             }
        return Response(data)

def create_unified_data():

    # At this stage, all objects are constructed and stored in DB. So now we wil
    # nest back the objects instances. So that the data can be exported as unfified

    industry_query = Industry.objects.all()
    for industry in industry_query:
        industry_quarter_query = Industry_Quarters.objects.filter(industry=industry.name)
        industry_quarter_query_json = serializers.serialize('json', industry_quarter_query)
        industry.industry_Performance_List = industry_quarter_query_json
        industry.save()

        company_query = Company.objects.filter(industry=industry.name)
        for company in company_query:

            clients_query = Client.objects.filter(company=company)
            clients_query_json = serializers.serialize('json', clients_query)
            company.client_list = clients_query_json

            employee_query = Employee.objects.filter(company=company)
            employee_query_json = serializers.serialize('json', employee_query)
            company.employee_list = employee_query_json

            company.save()

    print("HELP VEN")

#=====================================================================================

create_unified_data()