###Application setup order 
Create migrations and apply them to database   
+ `python manage.py makemigrations`  
+ `python manage.py migrate`  

Create permission groups: __clients, administrators, managers__. 
All users will have client's permissions.  
+ `python manage.py create_groups`  

Create superuser __admin:admin__  
+ `python manage.py create_superuser`  

###API
`http://127.0.0.1:8000/api`  
Client API:  
`http://127.0.0.1:8000/api/workers` -  list of workers
`http://127.0.0.1:8000/api/workers/?speciality=Synthetic limb replacer` -  list of exact speciality workers
`http://127.0.0.1:8000/api/workers/1` -  worker
`http://127.0.0.1:8000/api/workers/1/?date=2022-11-21` -  list of work hours for selected worker and date  
Manager API:  
`http://127.0.0.1:8000/api/locations/` -  CRUD
`http://127.0.0.1:8000/api/workers/` -  CRUD
`http://127.0.0.1:8000/api/schedules/` -  CRUD based on locations and workers
Administrator API:  
`http://127.0.0.1:8000/api/users/` -  list of users
`http://127.0.0.1:8000/api/users/1/` -  user
`http://127.0.0.1:8000/api/appointments/` -  CRUD based on user and worker's schedule