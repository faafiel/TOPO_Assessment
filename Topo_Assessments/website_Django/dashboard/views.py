from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, FileResponse
from django.template import RequestContext

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import JsonResponse
from dashboard.models import *
from .serializers import *
from .utils import *
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
            tmp = str(year[counter]) + "_" + str(quarter[counter])
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

        print(c2_chart_data)
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

class Export(APIView):

    def get(request, file_name='unified_Data.json'):
        print("help")
        BASE_DIR = Path(__file__)
        print(BASE_DIR)
        file_path = os.path.join(BASE_DIR, '.', file_name)
        print("help")
        print(file_path)
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
        else:
            # Handle file not found error
            pass
