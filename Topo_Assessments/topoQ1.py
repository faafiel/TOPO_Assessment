import pandas as pd
import numpy as np
import json
from IPython.display import display
import pdfplumber
from pptx import Presentation

'''
    The code comprises a series of class instances that are nested into one another: 

    industry class (Superclass)
     - Industry Quarter performance class
     - company class 
        - clients class
        - employee class
        - Annual Performance class
           - Quarter Performance class

    The Importer class imports the 4 datasets and uses the data to construct other class instances which are nested. The
    nested structure is then converted into a unified dictionary structure and exported as a json file in local directory.

    Each class except Importer class has a Get_Dict() function that reformats the instance into a subset of the 
    unified dictionary, before being merged with the dictionary of it's parent class.


    '''
#===========================================================================================================================
# Class' 

    
class Industry:
    def __init__(self, name, industry_Performance_List, company_List):
        self.name                       = name
        self.industry_Performance_List  = industry_Performance_List # 2D array of: [Year] BY [Quarter, Revenue, Memberships sold, AVG Duration(Minutes)]
        self.company_List               = company_List              # 1D array of Company objects

    def Get_Dict(self):
        json_Company_List = []
        json_Industry_Performance_List = []

        for company in self.company_List:
            json_Company_List.append(company.Get_Dict())

        for quarter in self.industry_Performance_List:

            json_quarter = {"year": quarter[0],
                            "quarter": quarter[1],
                            "revenue": quarter[2],
                            "memberships_Sold": quarter[3],
                            "avg_Duration_Mins": quarter[4]}
            
            json_Industry_Performance_List.append(json_quarter)

        dict_obj = {
            "name": self.name,
            "industry_Performance_List": json_Industry_Performance_List,
            "company_List": json_Company_List
        }
        return dict_obj

class Company:
    def __init__(self, id, name,  employee_List, q_Performance_List, industry = "Nan", company_Revenue = "NaN",  location = "NaN", client_List = "NaN"):
        self.id                         = id
        self.name                       = name
        self.industry                   = industry
        self.company_Revenue            = company_Revenue
        self.location                   = location
        self.employee_List              = employee_List            # 1D array of Employee objects
        self.q_Performance_List         = q_Performance_List       # 1D array of q_Performance objects
        self.client_List                = []                       # 1D array of client objects
        self.a_Performance_List         = []                       # 1D array of a_Performance objects

    def Client_Setter(self, client_List):
        self.client_List = client_List

    def Annual_Performance_Add(self, val):
        self.a_Performance_List.append(val)
    
    def Get_Dict(self):
        json_Employee_List      = []
        json_Q_Performance_List = []
        json_Client_List        = []
        json_A_Performance_List = []

        for employee in self.employee_List:
            json_Employee_List.append(employee.Get_Dict())

        for quarter in self.a_Performance_List:
            json_Q_Performance_List.append(quarter.Get_Dict())
        
        for client in self.client_List:
            json_Client_List.append(client.Get_Dict())

        for annual in self.a_Performance_List:
            json_A_Performance_List.append(annual.Get_Dict())

        dict_obj = {
            "id": self.id,
            "name": self.name,
            "industry": self.industry,
            "company_Revenue": self.company_Revenue,
            "location": self.location,
            "employee_List": json_Employee_List,
            "q_Performance_List": json_Q_Performance_List,
            "client_List":  json_Client_List,
            "a_Performance_List": json_A_Performance_List
        }
        return dict_obj

class Client:
    def __init__(self, date, membership_Id, membership_Type, activity, revenue, duration_Min, location ):
        self.date                       = date
        self.membership_Id              = membership_Id
        self.membership_Type            = membership_Type
        self.activity                   = activity
        self.revenue                    = revenue
        self.duration_Min               = duration_Min
        self.location                   = location

    def Get_Dict(self):
        dict_obj = {
            "date": self.date,
            "membership_Id": self.membership_Id,
            "activity": self.activity,
            "revenue": self.revenue,
            "duration_Min": self.duration_Min,
            "location": self.location
        }
        return dict_obj

class Employee:
    def __init__(self, id, name, role = "NaN", cashmoney = "NaN", hired_Date = "NaN"):
        self.id                         = id
        self.name                       = name
        self.role                       = role
        self.cashmoney                  = cashmoney
        self.hired_Date                 = hired_Date

    def Get_Dict(self):
        dict_obj = {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "cashmoney": self.cashmoney,
            "hired_Date": self.hired_Date
        }
        return dict_obj
    
class Q_Performance: 
    def __init__(self, year = "Nan", quarter = "NaN", memberships_Sold = "NaN", avg_Duration_min = "NaN", revenue = "NaN", profit_Margin = "NaN"):
        self.year                       = year
        self.quarter                    = quarter           # This should be a string for compatibility with different documents
        self.revenue                    = revenue
        self.memberships_Sold           = memberships_Sold
        self.avg_Duration_min           = avg_Duration_min
        self.profit_Margin              = profit_Margin

    def Get_Dict(self):
        dict_obj = {
            "year": self.year,
            "quarter": self.quarter,
            "memberships_Sold": self.memberships_Sold,
            "avg_Duration_min": self.avg_Duration_min,
            "revenue": self.revenue,
            "profit_Margin": self.profit_Margin
        }
        return dict_obj

class A_Performance:
    def __init__(self, year, total_Revenue, total_Membership_Sold, top_Location, quarters, revenue_Distribution):
        self.year                       = year
        self.total_Revenue              = total_Revenue
        self.total_Membership_Sold      = total_Membership_Sold
        self.top_Location               = top_Location
        self.quarters                   = quarters              # 1D array of Q_Performance objects
        self.revenue_Distribution       = revenue_Distribution  # 1D arrary of [gym, pool, tennis_Court, personal_Training]

    def Get_Dict(self):
        json_Revenue_Distribution = {"gym": self.revenue_Distribution[0],
                                     "pool": self.revenue_Distribution[1],
                                     "tennis_Court": self.revenue_Distribution[2],
                                     "personal_Training": self.revenue_Distribution[3]}
        
        json_Quarter_List = []

        for quarter in self.quarters:
            json_Quarter_List.append(quarter.Get_Dict())

        dict_obj = {
            "year": self.year,
            "total_Revenue": self.total_Revenue,
            "total_Membership_Sold": self.total_Membership_Sold,
            "top_Location": self.top_Location,
            "quarters": json_Quarter_List,
            "revenue_Distribution": json_Revenue_Distribution
        }
        return dict_obj

class Importer:
    def __init__(self, file_JSON, file_CSV, file_PDF, file_PPTX):
        self.file_json = file_JSON
        self.all_Employee               = [] # temp 1D array of employee objects 
        self.all_Q_Performance          = [] # temp 1D array of performance objects
        self.all_Companies              = [] # temp 1D array of company objects
        self.all_Industry               = [] # 1D array of all industry

        self.Import_JSON(file_JSON)
        self.Import_CSV(file_CSV)
        self.Import_PDF(file_PDF)
        self.Import_PPTX(file_PPTX)


    def Import_JSON(self,  file):
        # Step 1: Import file as a dataframe
        df_json = pd.read_json(file)
        df_normalized = pd.json_normalize(
            df_json['companies']
        )

        # Step 2: Break down dataframe into smaller datasets, then construct objects to store said data
        # Step 2.1: Break down employee data by company
        for index, company in df_normalized.iterrows():
            employee_List = []
            for employees in company.employees:
                employee = []
                for attribute in employees.values():
                    employee.append(attribute)
                try:
                    employee_temp = Employee(employee[0],
                                    employee[1],
                                    employee[2],
                                    employee[3],
                                    employee[4])
                except:

                    employee_temp = Employee(employee[0],
                                    employee[1],
                                    employee[2],
                                    employee[3])
                employee_List.append(employee_temp)
            if len(employee_List) > 0:
                self.all_Employee.append(employee_List)
                
 

        # Step 2.2: Break down performance data by company
        with open('dataset1.json', 'r') as file:
            dict_json = json.load(file)
        
        for company in range(len(dict_json['companies'])):
            q_Performance = dict_json['companies'][company]["performance"]    # output is a 2 layer nested dictionary
            q_Performance_List = []
            for quarter in q_Performance:
                
 
                q_Performance_temp = Q_Performance( "NaN",
                                                   quarter,
                                                   "NaN",
                                                   "NaN",
                                                    q_Performance[quarter]['revenue'],
                                                    q_Performance[quarter]['profit_margin'])
                q_Performance_List.append(q_Performance_temp)
            self.all_Q_Performance.append(q_Performance_List)

        # Step 2.3: Break down company info data for each company
        selected_range = df_normalized.loc[:, 'id':'location'] 
        for index, company in selected_range.iterrows():
            
            attribute_List = []
            for attribute in company:
                attribute_List.append(attribute)
            
            company_temp = Company(attribute_List[0],
                            attribute_List[1],
                            self.all_Employee[index],
                            self.all_Q_Performance[index],
                            attribute_List[2],
                            attribute_List[3],
                            attribute_List[4])
            self.all_Companies.append(company_temp)

    def Import_CSV(self,  file):
        df_csv = pd.read_csv(file)
        client_List = []            # 1D array of Client objects
        for index, client in df_csv.iterrows():
            new_Client = []
            for attribute in client:
                new_Client.append(attribute)
            client_temp = Client(new_Client[0],
                            new_Client[1],
                            new_Client[2],
                            new_Client[3],
                            new_Client[4],
                            new_Client[5],
                            new_Client[6])
            
            client_List.append(client_temp)
        self.all_Companies[0].Client_Setter(client_List)

    def Import_PDF(self, file):
        with pdfplumber.open(file) as pdf:
            first_page = pdf.pages[0] 
            tables = first_page.extract_table()
            whole_page =  next(iter(first_page.extract_text_lines()))
            page_Header = whole_page.get('text')            # Finds first occurance of 'text' key in the page, returns value
            df_pdf = pd.DataFrame(tables[1:], columns= tables [0])
        industry_Performance_Historical = []                # 2D array of quarters 
        
        for index, years in df_pdf.iterrows():
            quarter_Performance = []
            for attribute in years:
                try:
                    attribute = attribute.replace(",", "")
                except ValueError:
                    tmp = []
                except AttributeError:
                    tmp = []

                try: 
                    attribute = int(attribute)
                except ValueError:
                    tmp = []
                except AttributeError:
                    tmp = []

                quarter_Performance.append(attribute)

            industry_Performance_Historical.append(quarter_Performance)

        # Create Industry Object and insert all other sub-objects

        self.all_Industry.append(Industry(page_Header, industry_Performance_Historical, self.all_Companies))


    def Import_PPTX(self, file):
       
        prs = Presentation(file)
        extracted_df = []       # 1D array to store all shapes extracted from PDF

        # Check for tables or text frames
        for slide in prs.slides:
            for shape in slide.shapes:
                if shape.has_table:
                    table = shape.table
                    data = []

                    # Extract data rows
                    for row in table.rows:#[1:]
                        row_data = [cell.text for cell in row.cells]
                        data.append(row_data)

                    # Convert to DataFrame
                    if data:
                        df = pd.DataFrame(data[1:], columns=data[0])
                        extracted_df.append(df)

                # Check for text boxes
                elif shape.has_text_frame:
                    text_frame = shape.text_frame
                    extracted_text = []
                    for paragraph in text_frame.paragraphs:
                        for run in paragraph.runs:
                            extracted_text.append(run.text)
                    extracted_df.append(extracted_text)

            
        first_Shape = extracted_df[0]

        # Page 1 of PPTX
        report_Year = int(extracted_df[0][0][-4:]) 
        total_Revenue = int(extracted_df[1][1][16:].replace(",", ""))
        total_Membership_Sold = int(extracted_df[1][2][24:].replace(",", ""))
        top_Location = extracted_df[1][3][14:]

        # Page 2 of PPTX
        q_Performance_List = []
        
        for index, quarters in extracted_df[3].iterrows():
            q_Performance_temp = Q_Performance( report_Year,
                                                   quarters.iloc[0],
                                                   int(quarters.iloc[2]),
                                                   int(quarters.iloc[3]),
                                                   int(quarters.iloc[1].replace(",", "")))
            
            q_Performance_List.append(q_Performance_temp)         

        # Page 3 of PPTX
        distribution_List = []
        distribution_List.append(int(extracted_df[5][1][5:7]))
        distribution_List.append(int(extracted_df[5][2][6:8]))
        distribution_List.append(int(extracted_df[5][3][14:16]))
        distribution_List.append(int(extracted_df[5][4][19:21]))
        
        annual_temp = A_Performance(report_Year, 
                                    total_Revenue,
                                    total_Membership_Sold,
                                    top_Location,
                                    q_Performance_List,
                                    distribution_List )
        self.all_Industry[0].company_List[0].Annual_Performance_Add(annual_temp)
    
    def Export (self):
        file = self.all_Industry[0].Get_Dict()
        with open('unified_Data.json', 'w') as json_file:
            json.dump(file, json_file, indent=4)

#===========================================================================================================================

import_Temp = Importer("dataset1.json", "dataset2.csv", "dataset3.pdf", "dataset4.pptx")
import_Temp.Export()

