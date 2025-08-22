from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import JsonResponse
from dashboard.models import *
from .serializers import *
from .utils import *

# def index(request):
#     return render(request, 'index.html')



def index_page(request):
    return render(request, 'index.html')

def charts_page(request):
    template = loader.get_template('charts.html')
    return HttpResponse(template.render())

#==================================================================================================
# def get_industry_quarter_chart(request):
#     print("printing help")

#     query_set = Industry_Quarters.objects()
#     print(query_set)

#     quarter_list = []
#     revenue_list = []

#     for obj in query_set:
#         quarter_list.append(obj.quarter)
#         revenue_list.append(obj.revenue)


#     return render(request, 'index.html',{'labels':quarter_list,
#                                          'revenue':revenue_list})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
 
    def get(self, request, format = None):

        quarter = Industry_Quarters.objects.values_list('quarter')
        year = Industry_Quarters.objects.values_list('year')
        revenue = Industry_Quarters.objects.values_list('revenue')
        print(revenue)

        quarter_year = []
        counter = 0
        for each in quarter:
            tmp = str(year[counter]) + "_" + str(quarter[counter])
            tmp.replace(",", "")
            tmp.replace("'", "")
            tmp.replace("(", "")
            tmp.replace(")", "")
            print(type(tmp))
            quarter_year.append(tmp)
            counter += 1

        revenue_list = []
        rev_counter = 0
        for each in revenue:
            tmp = str(revenue[rev_counter])
            tmp.replace(",", "")
            rev_counter += 1

        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data ={
                     "labels":quarter_year,
                     "chartLabel":chartLabel,
                     "chartdata":revenue,
             }
        return Response(data)