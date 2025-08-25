INTRO 

Project is a uv venv that contains a django project. 

To localhost the django project:

_Setting up_
1) cd to your equivalent address of "cd C:\Users\USER\OneDrive\12.Github_repos\Topo_Assessments\website_Django". This is the directory structure.
2) Run "python manage.py makemigrations"
3) Run "python manage.py migrate"
4) Run "python manage.py makemigrations dashboards 0021"
   
   - NOTE: The 0021 may be different on different machines. It may be 0001 or 0022 on a new machine. Please check "migrations" folder in directory to verify the number of the latest file 
   - The format for this CLI is "python manage.py makemigrations dashboards <migration_prefix>"
  
_Start Server_

5) python manage.py runserver    

_Localhost address_

6) http://127.0.0.1:8000/index/


TODO

- Fix HTML titles
- Fix filter bug
- Fix export bug
