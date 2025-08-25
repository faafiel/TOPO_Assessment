from django.urls import path
from dashboard.views import *
from dashboard import views


urlpatterns = [
    path('', views.index_page, name='home'),
    # path("charts/", charts_page, name = "charts_page"),
    path("index/", index_page, name = "index_page"),
    path('chart_data', views.ChartData.as_view()),
    # path('export_json', views.Export.as_view()),

]
 