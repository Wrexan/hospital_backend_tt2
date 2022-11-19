###Application setup order 
Create migrations and apply them to database   
+ `python manage.py makemigrations`  
+ `python manage.py migrate`  

Create permission groups: __clients, administrators, managers__. 
All users will have client's permissions.  
+ `python manage.py create_groups`  

Create superuser __admin:admin__  
+ `python manage.py create_superuser`  
