steps to run the project successfully 
1- activate the virtual environment through running the following command in terminal 
    venv\Scripts\activate      
2- install all the needed packages that are specified in the requirements.txt file through running the following command in terminal 
    pip install -r requirements.txt  
3- make the migrations of the project through the steps :
    3.1- navigate to the file settings.py in the backend folder 
    3.2- navigate to the DATABASES section (in the line 91)
    3.3- change the variables to be compatible with your MySql workbench configuration 
    3.4- run the following command in the terminal 
        python manage.py makemigrations    
4- migrate with the database through running the following command in terminal 
    python manage.py migrate   
5- run the server through running the following command in terminal 
    python manage.py runserver 