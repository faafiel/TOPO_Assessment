OVERVIEW

This repo hosts a uv venv that contains a django project. Briefly, the recurring solution to problems can be described as constant data massaging, and packing/unpacking data as a consolidated package wherever possible to simplify the codebase

ELABORATION

To solve the import challenge, I converted the data from the datasets into python objects (Industry, Company, Employee, Client, Annual_Performance ... etc ) that were nested together. This unified structure was then exported into a local file directory in JSON

I used Django to host the website; which imported the locally stored unified data JSON file upon every server startup. So data is overwritten every time. The Django database is sqlite3. The JSON data is again broken down to create objects which populate the DB. 

Data routed from DB to frontened was consolidated into 1 package, then unpacked at frontend. 

At this stage user should be in the index.html which can further access the admin page which has a UI/UX for the database. 
From admin page, it is possible to import/export ALL Industry objects (in various formats) which will export the entire DB as a unified structure. Alternatively, it is possible to import/export the nested class instances such as Company, Annual_Performance etc which will also include their respective nested objects (related via foreign key).

DJANGO PORJECT:
_Setting up_

1) The entire folder "TOPO assessments" contains the UV venv, MCP, data importation script, and Django website. The instructions below are within the context of my local directory, so some localization is necessary. It will be necessary to initate and popualte DB, and import library as per pyproject.TOML file. DB population can only be done after running python scripts!

2) cd to "C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments" or equivalent. 
3) Run the "main.py" file. This will handle data importing and produce a "unified_Data.json" file at "C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django\dashboard". At this stage, we have the data to start Django server
2) cd to your equivalent address of "cd C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django". This is the directory structure.
3) Run CLI "python manage.py makemigrations". This will generate a commit request for frontend DB UI/UX
4) Run CLI "python manage.py makemigrations dashboards 0028". This will generate a commit request for DB creation

   - NOTE: The 0028 may be different on different machines. It may be 0001 or 0029 on a new machine. Please check "migrations" folder in directory to verify the number of the latest file 
   - The format for this CLI is "python manage.py makemigrations dashboards <migration_prefix>"

5) Run CLI "python manage.py migrate". commit latest migration
   
_Start Server_

1) cd to "C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django" or equivalent, where the manage.py file is located
2) run CLI "python manage.py runserver"    

_Localhost address_

1) Got to http://127.0.0.1:8000/index/ on browser

_Exporting/Importing_

1) Importing is done automatically upon server startup using a data file from local directory
2) But to manually import/export, naviagte to the admin page on the localhost and login

   - Password: topo1234 
   - User: Amir

3) Then navigate to the models(objects) in DB that want to be exported/imported. To export entire DB, export 
   ALL "Industry" class.

   DASHBOARD VIEW: CHARTS
   
   <img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/88e8c4c3-8dbe-462c-91a8-b076fb6c31aa" />
   

   ADMIN VIEW: AND DB UI/UX
   
   <img width="1400" height="600" alt="image" src="https://github.com/user-attachments/assets/63e8d83d-fe57-494d-a200-0831359c8d5d" />
   

   ADMIN VIEW: ONE WAY TO EXPORT
   
   <img width="1100" height="400" alt="image" src="https://github.com/user-attachments/assets/1284ac8a-6244-4014-a453-db0cd8a53f54" />

   ADMIN VIEW: EXPORT OPTIONS

   <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/91996efb-1d5a-4a31-86e9-bc4cf19e758a" />

   

   ADMIN VIEW: INDIVIDUAL RECORDS
   
   <img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/b0e20e62-f6b3-426a-ac84-904c519df11e" />
   

   ADMIN VIEW: LOGIN
   
   <img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/7bc16053-96fb-4fb3-b65d-c2d51c52b6d5" />




CHALLENGES

1) New libraries and new library functions related with frontend. DB table population and importing/exporting functionality was the most time consuming blocker 
