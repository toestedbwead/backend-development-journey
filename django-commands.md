# creates boilerplate django files
django-admin startproject <project-name>

# creates app folder and files
python manage.py startapp <app-name>

# preps our database for migrations
python manage.py makemigrations

# executes our migrations & updates the database
python manage.py migrate

# creates a user with admin level permissions
python manage.py createsuperuser