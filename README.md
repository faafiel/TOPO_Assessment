INTRO 

This repo hosts a uv venv that contains a django project. 

To localhost the django project:

_Setting up_

1) cd to your equivalent address of "cd C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django". This is the directory structure.
2) Run CLI "python manage.py makemigrations". This will generate a commit request for frontend
3) Run CLI "python manage.py makemigrations dashboards 0026". This will generate a commit request for DB

   - NOTE: The 0021 may be different on different machines. It may be 0001 or 0027 on a new machine. Please check "migrations" folder in directory to verify the number of the latest file 
   - The format for this CLI is "python manage.py makemigrations dashboards <migration_prefix>"
5) Run CLI "python manage.py migrate". commit latest migration
   
  
  
_Start Server_

5) python manage.py runserver    

_Localhost address_

6) http://127.0.0.1:8000/index/

_Exporting_

7) To export, naviagte to the admin page and login

   - Password: topo1234 
   - User: Amir

8) Open up Industry table by selecting "Industrys"
9) Open up an industry record and find the export button at the bottom. Alternatively, you may export from the Industry table view

TODO

- Fix HTML titles
