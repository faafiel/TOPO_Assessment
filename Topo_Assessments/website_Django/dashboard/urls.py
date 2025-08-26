from django.urls import path
from dashboard.views import *
from dashboard import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path("index/", index_page, name = "index_page"),
    path('chart_data', views.ChartData.as_view()),
]
 