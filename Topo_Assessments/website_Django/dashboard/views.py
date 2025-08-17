from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from dashboard.models import *
from .serializers import Item_Serializer

# def index(request):
#     return render(request, 'index.html')

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

# @api_view(['GET'])
# def getData(request):
#     items = Item.objects.all()
#     serializer = Item_Serializer(items, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addItem(request):
#     serializer = Item_Serializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# def import_data(request):
#     if request.method == 'POST' and request.FILES['json_file']:
#         json_file = request.FILES['json_file']
#         data = json.load(json_file)
#         for item in data:
#             book = Book(
#                 title=item['title'],
#                 author=item['author'],
#                 publication_year=item['publication_year']
#             )
#             book.save()
#         return render(request, 'success.html')
#     return render(request, 'form.html') 