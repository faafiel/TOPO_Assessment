"""
URL configuration for website_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from dashboard.views import *
from dashboard import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path("charts/", charts_page, name = "charts_page"),
    path("index/", index_page, name = "index_page"),
    path('api', views.ChartData.as_view()),

    # path("dashboard/industry_quarter/", views.get_industry_quarter_chart, name="industry_quarter_chart")
    # path("chart/filter-options/", views.get_filter_options, name="chart-filter-options"),
    # path("chart/sales/<int:year>/", views.get_sales_chart, name="chart-sales"),
    # path("chart/spend-per-customer/<int:year>/", views.spend_per_customer_chart, name="chart-spend-per-customer"),
    # path("chart/payment-success/<int:year>/", views.payment_success_chart, name="chart-payment-success"),
    # path("chart/payment-method/<int:year>/", views.payment_method_chart, name="chart-payment-method"),
    ]