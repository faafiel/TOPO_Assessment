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
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def charts_page(request):
    template = loader.get_template('charts.html')
    return HttpResponse(template.render())

#==================================================================================================
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
 
    def get(self, request, format = None):
        quarter_labels = [
                        '2022 Q1',
                        '2022 Q2,'
                        '2022 Q3',
                        '2022 Q4',
                        '2023 Q1',
                        '2023 Q2,'
                        '2023 Q3',
                        '2023 Q4',
                        '2024 Q1',
                        '2024 Q2,'
                        '2024 Q3',
                        '2024 Q4'
                        ]
        
        revenue = Industry_Quarters.objects.values('revenue').all()
        quarter_list = Industry_Quarters.objects.values('quarter', 'revenue').all()
        
        print(quarter_list)
        print("HI:")
        data ={
                     "labels":quarter_labels,
                     "chartLabel":"Industry Performance per quarter",
                     "chartdata":quarter_list,
             }
        return Response(data)