"""Introduction

Django is a web based application written in Python Programming.It is based on MVT(Model View Template) design pattern.
By using django we can build web applications.

Django Features
1. Rapid Development
2. Secure
3. Scalable
4. Fully loaded
5. Versatile
6. Open Source

Django Project contains following packages and files. The directory is just a container for the application.

1. manage.py: It is a command line utility which allows us to interact with the project, it is used to manage
application.
2. __init.py__ : It is an empty file that tells to the Python that this directory should be considered as a Python
Package.
3. settings.py: This file is used to configure application such as database connection, static files linking etc.
4. urls.py: We can mention the URLs and corresponding actions to perform the task and display the view.
5. wsgi.py: It is an entry point for WSGI-compatible web servers to serve Django Project.

Django Configuration with Apache Web Server

Django uses its built-in development server to run the web application.
To start this server, we can use python manage.py runserver command.

This command starts the server which runs on ports 8000 and can be accessed at browser by entering
localhost:8000. It shows a welcome page of the application.

But if we want to run our application by using apache server rather than built in development server, we need to
configure apache2.conf file located at /etc/apache directory. Add the following code into this file.

//apache2.conf
WSGIScriptAlias //var/www/html/django7/django7/wsgi/py
WSGIPythonPath /var/www/html/django7

<Directory /var/www/html/django7>
        <Files wsgi.py>
                Require all granted
        </Files>
</Directory>

After adding these lines, restart apache server by using the service apache2 restart command and the type
localhost to the browser's address bar. This time, project will run on apache server rather than a built-in
server.

Django Virtual Environment SetUp

The virtual environment is an environment which is used by Django to execute an application. It is recommended
to create and execute a Django application in a separate environment. Python provides a tool
virtualenv to create an isolated Python environment.

1. Install package
apt-get install python3-venv

2. Create Directory
mkdir django7

3. Create Virtual Environment
python3 -m venv django7

4. Activate Virtual Environment
After creating a virtual environment,activate it by using the following command.
source djangoenv/bin/activate

Django Admin Interface
Django provides a built-in admin module which can be used tp perform CRUD operation on the models. It reads
metadata from the model to provide a quick interface where an user can manage the content of the application.
This is a built-in module and designed to perform an admin related tasks to the user.

The admin app (django.contrib.admin) is enabled by default and already added into INSTALLED_APPS section of the settings
file. To access it at browser use '/admin/ at a local machine like localhost:8000/admin/.
Create an Admin user -> python3 manage.py createsuperuser

It is a Django Admin Dashboard. Here, we can add and update the registered models.

Django MVT(Model View Template)
The MVT(model view template) is a software design pattern. It is a collection of three important components Model
View and Template. The model helps to handle databases. It is a data access layer which handles the data.

The template is a presentation layer which handles User Interface part completely. The view is used to execute the
business logic and interact with a model to carry data and renders a template.
There is no separate controller and complete application is based on Model View and Template.
Here, an user requests for a resource to the Django, Django works as a controller and check to the available
resource in URL. If URL maps, a view is called that interact with model and template, it renders a template.
Django responds back to the user and sends a template as a response.

Django Model
In Django, model is a class which is used to contain essential fields and methods.
Each model class maps to a single table in the database. Django Model is a subclass of Django.db.models.Model
and each field of the model class represents a database field(column).
Django provides us a database-abstraction API which allows us to create,retrieve,update and delete a record
from the mapped table. Model is defined in Models.py file.

Register/Use Model
After creating a model, register model into the INSTALLED_APPS inside SETTINGS.PY.

Django Model Fields
The fields defined inside the Model class are the columns name of the mapped table. The field name shouls not be
python reserve words like clean, save or delete etc.
Django provides various built-in field types.
1. Auto Field
2. Binary Field
3. Char Field
4. DateTimeField
5. EmailField
6. Image Field
7. FileField
8. TextField

Field Options
Each field requires some arguments that are used to set column attributes.
Common attributes available to all field types:
1. Null : Django will store empty values as NULL in the database.
2. Blank : It is used to allowed field to be blank.
3. Choices : An iterable(e.g. Tuple or List) of 2 -tuples to use as choices for this field.
4. Default : The default value for the field. This can be a value or callable object.
5. Primary_key : This field is the primary key for the model.
6. Unique : The field must be unique throughout the table.

Django Views
A view is a place where we put our business logic of the application. The view is a python function which is used to perform
some business logic and return a response to an user. This response can be the HTML contents if the Web page,
or a redirect, or a 404 error.

Returning Errors
Django provides various built in error classes that are subclass of the HttpResponse and use to show
error message as HTTP response. Some classes are listed below:

Class                           Description
class                       It is used to designate that a page hasn't been modified since the user's last request
HttpResponseNotMethod       (status code: 304)
class                       It acts just like HttpResponse but uses a 400 status code.
HttpResponseBadRequest
class                       It acts just like HttpResponse but used a 404 status code.
HttpResponseNotFound
class                       It acts just like HttpResponse but uses a 410 status code.
HttpResponseNotAllowed
HttpResponseServerError     It acts just like HttpResponse but uses a 500 status code.

Django View HTTP Decorator
Http Decorators are used to restrict access to view based on the request method. These decorators are listed
in django.views.decorators.http and return a django.http.HttpResponseNotAllowed if conditions are not met.

Django Template
Generate dynamic HTML pages by using its template system.
A template consists of static parts of the desired HTML output as well as some special syntax describing
how dynamic content will be inserted.

Why Django Template?
In HTML file, we don't write python code because the code is only interpreted by python interpreter
not the browser. Django template engine is used to separate the design from the python code
and allows us to build dynamic web pages.

Django Template Configuration
To configure the template system, we have to provide some entries in settings.py file.

TEMPLATES = [
    {
        'BACKEND' : 'django.templates.backends.django.DjangoTemplates',
        'DIRS' : [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS' : True,
        'OPTIONS' : {
            'context_processors' : [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
         },
     },
]

Here, we mentioned that our template directory name is templates. By default, Django Templates looks for
a templates subdirectory in each of the INSTALLED_APPS.

Django Template Simple Example
First,create a directory template inside the project.

Django Template Language
Django template uses its own and syntax to deal with variable, tags , expression etc. A template is rendered
with a context which is used to get value at a web page.

Variables
Variables associated with a context can be accessed by {{}} (double curly braces). For example, a variable name
is rahul. Then the following statement will replace name with its value.
Example :  My name is {{name}}. My name is rahul.

URL Mapping
Since, Django is a web application framework,it gets user requests by URL Locator and responds back. To handle
URL, django.urls module is used by the framework.

//urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/',admin.site.urls)
]

Django already has mentioned an URL here for the admin. The path function takes the first argument
as a route of string or regex type. The view argument is a view function which is used to return a response
(template) to the user. The django.urls module contains various functions, path(route,view,kwargs,name) is
one of those which is used to map the URL and call the specified view.

Django Static File Handling
The django.contrib.staticfiles modules to help them.

Django Static(CSS,JavaScript,image) Configuration
1. Include the django.contrib.staticfiles into INSTALLED_APPS.
2. Define STATIC_URL in settings.py file.
STATIC_URL = '/static/'
3. Load static files in the template by using below expressions.
{% load static %}
4. Store all images,JavaScript,CSS files in a static folder of the application.

ModelForms
It is a class which is used to create an HTML form by using the model. It is an efficient way to create a form
without writing an HTML code.
Django provides a helper class which allows us to create a Form class from a Django model.

DjangoForms
Django provides a Form class which is used to create HTML forms. It describes a form and how it work and appears.
It is similar to the ModelForm class that creates a form ny using the Model, but it does not require the Model.
Each field of the form class map to the HTML form <input> element and each one is a class itself, it manages form
data and performs validation while submitting the form.
Note: Django Form does not include <form> tags, or a submit button. We will have to provide those ourselves
in the template.
Commonly, user field and their fields:
1. CharField
2. ChoiceField
3. DateField
4. DateTimeField
5. Image Field
6. File Filed
7. DecimalField
8. Email Field

FormValidation
Django provides a built in methods to validate form data automatically. Django forms only submit if its only contains
CSRF tokens. It uses a clean and easy approach to validate data.
The is_valid() method is used to perform validation for each field of the form, it is defined in Django Form class.
It returns True if data is valid and placed all data into a cleaned_data attribute.

FileUpload
File upload to the server using Django is very easy task. Django provides built-in library methods that
help to upload a file to the server. The forms.FileField() methods is used to create a file input and submit the
file to the server. While working with files, make sure the HTML form tag contains enctype="multipart/form-data"
property.

Django Database Connectivity
The settings.py file contains all the project settings along with database connection details. By default, Django
works with SQLite, database and allows configuring for other databases as well.
Database connectivity requires all the connection details such as database name,user credentials,
hostname driver name etc. To connect with MySQL, django.db.backends.mysql driver is used to establishing a
connection between application and database. We need to provide all connections details in the settings file.
The settings.py file of our project contains the following code for the database.

DATABASES = {
    'default' {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'djangoApp',
        'USER' : 'root',
        'PASSWORD' : 'mysql',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }
}

After providing details, check the connection using migrate command.
$ python3 manage.py migrate
This command will create tables for admin,auth,contenttypes and sessions. Now,access to the MySQL database
and see the database from the list of database. The created database contains the tables.
Note: It throws an error if database connectivity fails: django.db.utils.OperationalError: (1045, "Access
denied for user 'root'@'localhost' (using password: YES)").

Migrating Model
Each Django's model is mapped to a table in the database. So after creating a model, we need to migrate it.
Django first creates a migration file that contains the details of table structure.
python3 manage.py makemigrations

Django Database Migrations
Migration is a way of applying changes that we have made to a model, into the database schema. Django creates
a migration file inside the migration folder for each model to create the table schema, and each table is mapped
to the model of which migration is created.
Django provides the various commands that are used to perform migration related tasks. After creating a model,
we can use these commands.
-> makemigrations : It is used to create a migration file that contains code for the tabled schema of a model.
-> migrate : It creates table according to the schema defined in the migration file.
-> sqlmigrate : It is used to show a raw SQL query of the applied migration.
-> showmigrations : It lists out all the migrations and their status.

Django Middleware
In Django, middleware is a lightweight plugin that processes during request and response execution. Middleware
is used to perform a function in the application. The functions can be a security,session,csrf protection,
authentication. Django provides a built-in middleware and also allows us to write our own middleware.
Middleware used to provide functionalities to the application. Security Middleware is used to maintain the security
of the application.

Middleware Ordering and Layering
Middleware applies in the order it is defined in MIDDLEWARE list and each middleware class is a layer. The
MIDDLEWARE list is like each request passes through from top to bottom and response is in reverse order(bottom to up).
Other Middleware Methods
Apart from request and response, we can add three methods to add three more methods to add more features:
1. process_view(request,view_func,view_args,view_kwargs)
It takes HttpRequest object,function object,list of arguments passed to the view or a dictionary of arguments
respectively. This method executes just before the calling the view. It returns either None or HttpResponse, it
stops processing and return the result.
2. process_template_response(request,response)
It takes 2 arguments first is a reference of HttpRequest and second is HttpResponse object. this method is called
just after the view finished execution. It returns a response object which implements the render model.
3. process_execution(request,exception)
This method takes two arguments, first is HttpRequest object and second is Exception class object that us raised
by the view function. This method returns None or HttpResponse object. if it returns a response, the middleware
will be applied and the result returns to the browser. Otherwise, the exception is handle by default handling system.

Django Request and Response
The client-server architecture includes two major components requests and response. The Django framework uses
client-server architecture to implement web applications. When a client requests for a resource, a HttpRequest
object is created and correspond view function is called that returns httpResponse object.
To handle request and response, Django provides HttpRequest and HttpResponse classes. Each class has its own
attributes and methods.

Django HttpRequest
This class is defined in the django.http module and used to handle the client request.
Django HttpRequest Attributes
Attribute                               Description
HttpRequest.GET             It returns a dictionary-like object containing all given HTTP GET parameters.
HttpRequest.POST            It is a dictionary-like object containing all given HTTP POST parameters.
HttpRequest.COOKIES         It returns all cookies available
HttpRequest.FILES           It contains all uploaded files.

Django HttpRequest Methods
Attribute                                            Description
HttpRequest.get_host()            It returns the original host of the request.
HttpRequest.get_port()            It returns the originating port of the request.
HttpRequest.get_full_path()       It returns the path,plus an appended query string.
HttpRequest.build_absolute_uri    It returns the absolute URI form of location.
(location)
HttpRequest.is_secure()            It returns True if the request is secure; that is, if it was made with HTTPS.

Django HttpResponse
This class is a part of django.http module. It is responsible for generating responds corresponds to the request
and back to the client.































"""