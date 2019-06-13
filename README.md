# podverse-admin

This is a Python Django project that provides a UI for making database updates.

The project uses its own database (podverse_django_admin_db) for managing authentication into the admin interface, and connects to the Podverse database (podverse_db) to make updates. This project also adds a 

NOTE: This Django app should not be used to manage podverse_db migrations. The podverse_db models are managed in the podverse-api application. 

You'll need to make sure you have [Python and virutalenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) setup properly, and your virtualenv activated within the project directory.

For more information on Django please refer to its [documentation](https://docs.djangoproject.com/en/2.2/intro/tutorial01/).

## install dependencies
`pip install -r requirements.txt`

## run migrations
`python manage.py migrate`

## update migrations
If any models change, you will need to create a new migration by running:
`python manage.py makemigrations`

Then run `python manage.py migrate`

## create permissions and groups
`python manage.py create_permissions_and_groups`

## create a superuser
`python manage.py createsuperuser`

## run the app for local development
`python manage.py runserver`
