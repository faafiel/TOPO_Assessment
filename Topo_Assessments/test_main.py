from main import *
from topoQ1 import *

dummy_indutry_performance_list = [
        {
            "year": 2077,
            "quarter": "Q1",
            "revenue": 69,
            "memberships_sold": 420,
            "avg_duration_mins": 6
        },
        {
            "year": 2077,
            "quarter": "Q2",
            "revenue": 420,
            "memberships_sold": 69420,
            "avg_duration_mins": 9
        },
        {
            "year": 2077,
            "quarter": "Q3",
            "revenue": 69420,
            "memberships_sold": 69,
            "avg_duration_mins": 42
        }]

dummy_company_list = ['micheal', 'scott']

test_industry_obj = Industry ("name", dummy_indutry_performance_list, dummy_company_list)


def test_industry_get_dict():
    assert test_industry_obj.get_dict()