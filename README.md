OVERVIEW

This repo hosts a uv venv that contains a django project. Briefly, the solution can be described as constant data massaging, and handling data as a consolidated package wherever possible to simplify the codebase

ELABORATION

To solve the import challenge, I converted the data from the datasets into python objects (Industry, Company, Employee, Client, Annual_Performance ... etc ) that were nested together. This unified structure was then exported into a local file directory in JSON

I used Django to host the website; which imported the locally stored unified data upon every server startup. So data is overwritten. The Django database is sqlite3. The JSON data is again broken down to create objects which populate the DB. 

Data routed from DB to frontened was consolidated; then unpacked at frontend. Chart filtering was done via updating. 

At this stage user should be in the index.html which can further access the admin page which has a UI/UX for the database. 
Fromo admin page, it is possible to import/export Industry (in various formats) which will export the entire DB as a unified structure. Alternatively, it is possible to import/export the nested class instances such as Company, Annual_Performance etc which will also include their respective nested objects (related via foreign key).

To localhost the django project:

_Setting up_

1) cd to your equivalent address of "cd C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django". This is the directory structure.
2) Run CLI "python manage.py makemigrations". This will generate a commit request for frontend
3) Run CLI "python manage.py makemigrations dashboards 0026". This will generate a commit request for DB

   - NOTE: The 0028 may be different on different machines. It may be 0001 or 0029 on a new machine. Please check "migrations" folder in directory to verify the number of the latest file 
   - The format for this CLI is "python manage.py makemigrations dashboards <migration_prefix>"
5) Run CLI "python manage.py migrate". commit latest migration
   
  
  
_Start Server_

1) python manage.py runserver    

_Localhost address_

2) http://127.0.0.1:8000/index/

_Exporting/Importing_

1) It is done automatically upon server starup using a data file from local directory
2) But to manually import/export, naviagte to the admin page on the localhost and login

   - Password: topo1234 
   - User: Amir

   Then navigate to the models(objects) in DB that want to be exported/imported. To export/import entire DB, then export 
   ALL "Industry" class.

CHALLENGES

1) New libraries and new library functions with frontend