# PythonDjangoWebApp
A Full stack web development practice with python and Django


*I'm working on a Mac*
But to get started: 
1. I'm using python 3.7.0 & Django 2.1.7 in this repo
2. I also use pip as my package manager and start my project with
```
cd /Documents/Github/<repoName>
```
3. Then use 
```
django-admin startproject <projectName>
```
4. Gives a code skeleton that looks like:
```
.
├── djangoProject
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py 
```
   ###### __init__.py - empty file just to say that this is a python package
   ###### settings.py - settings and config (includes secret key, debug mode, app section, database settings, etc.)
   ###### urls.py - mapping url routes
   ###### wsgi.py - how the python web app communicates with the server
5. To start server, run
```
python manage.py runserver
```
   ###### Django is a web project, within in the web project could be multiple apps
   ###### example of an app could be a blog section, then a store section, etc.
   ###### apps are pretty much containable and shippable to other web projects, resuable
6. To start an app, run
```
python manage.py startapp <appName>
```
7. Gives a code skeleton that looks like:
```
.
├── README.md
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── djangoProject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
	- import modules such as: (inViews:[httpReponse, Render]) create a view
	- make urls.py file in app and include (inUrls:[include])
	- type out path pattern
	- type out path pattern in web project urls.py file
	- workflow:: add views for app-> update path patterns for app -> update webapp path patterns

8. Creating Templates in an app directory
###### instead of creating html for all views, we create <templates> sub-directory
###### inside of templates, new subdirectory in the name of our app (although redundant, makes things clear)
###### <whateverAppName> -> templates -> <whatverAppName> -> template.html
	- views.py -> render your html pages based on request
	- templates-> blog -> <filename>.html we can have base.html for repeat code
	- import bootstrap and custom.css for every item post
	- update routes based on what we click on navbar
	- also created dummy data as 'context'
9. To create a super user for the Administrator page, run
```
ptyhon manage.py makemigrations
python manage.py runserver
python manage.py createsuperuser
```
	- you can now login, in /admin page
	- click users to see your users
	- you can edit info, check current users/groups/etc. 
	- django doesnt store your actual passwords, it automatically hashes them
10. Create models class in your models.py file in your app directory
	- run python manage.py makemigrations
	- this creates a 0001_intial.py file under migrations sub-directory
	- to create this table in your database, run 
	```
	python manage.py sqlmigrate blog 0001
	python manage.py sqlmigrate <appName> <migrationNumber>
	``` 
	- After you create model class and create your table, run the migrate command 
	```
	python manage.py migrate
	```
	- Migrations are so useful bc they allow us to make changes to our databses even after its created and has existing data in the database
	- if you wanted to query the database using these models, you can access the shell by running
	```
	python manage.py shell
	```
	- example commands in the shell
	```
	from blog.models import Post
	from django.contrib.auth.models import User
	//query users table
	User.objects.all()
	User.objects.first()
	User.objects.filter(username='mastershefu') //or any other attribute
	//capture user object in variable
	user = User.objects.filter(username='mastershefu')
	//now you can take the variable and see all attributes of that user object
	user.id
	user.pk
	user = User.objects.get(id=1)
	//query posts 
	Post.objects.all()
	post_1 = Post(title = 'textbook 1', details = 'textbook for sale', price=40, author=user) //user must be declared beforehand
	//save your post object to your database
	post_1.save()
	//check if it saved by running
	Post.objects.all()
	//in order to get your post objects to show up in a more descriptive form, use the dunder str method (dunder means double underscore)
	post = Post.objects.first() 
	post.details
	post.price
	post.author.email
	//query all posts made by a specific user
	.modelname_set
	user.post_set
	user.post_set.all() 
	user.post_set.create(title = 'textbook 3', details = 'textbook for sale', price=120) //automatically saves
	```
	- go to app->views.py and replace dummy data with our post model
		- from .models import Post 
		- context -> posts -> Post.objects.all() 
		- to see the Post datatable in your /admin page, register it to your admin.py file in your app directory
		- import it again, then do admin.site.register(Post)

11. We have to create user registration, and we do this in a new app

	```python manage.py startapp users```
	- add to installed apps in settings.py file
	- add function to views to render register user page
	- add templates/users sub directory for html files
	- create html file for view function
	- update urls.py file 
	- go back to views.py file, now if your form as a POST method, 
	your function should take the request and post it to the database.
	- based on if the forms valid or not, we will both display success messages for the user and/or redirect them appropriately
	- if you want messages to work, climb through your hierarchy and code for the success messages in your base.html template
	- now that that works, you can save it to your database by adding form.save() in your register function in views.py
	- To customize what fields you want users to register with, create new forms.py file in your users app directory, then import and use the class in made in views.py
	- I'm using djangos "crispy-forms" to get a better styling
```pip install django-crispy-forms```
	- to use cripsy, list it in installed apps, dictacte which css framework youre using (both in settings.py file) then update your register.html file

12. We now have to create a login and logout system
	- update urls.py with auth_views login & logout
	- create login logout html files
	- create redirect links after form submissions
	- you can update your navbar for visual reinforcement of log in and log out actions
	- workflow review: views.py in app -> create  function to render page -> update project's urls.py file, create the html in template/appname directory
	- you can also restrict certain urls by making it so that we require an authentication/login before we access certain pages (for this you have to import decorators in your views.py file and update the link ur want redirection to in settings.py)

## How my file tree looks now
```
.
├── README.md
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       └── main.css
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       └── home.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── djangoProject
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    └── views.py
```
13. Creating user profiles and creating one to one relationship between users and profiles
	- create model in models.py file in user app sub directory
	- ```pip install Pillow```
	- ```python manage.py makemigrations```
	- ```python manage.py migrate```
	- register profile model in admin.py
	- run django shell 
	```
	python manage.py shell
	from django.contrib.auth.models import User
	user = User.objects.filter(username="mastershefu")
	user.profile
	user.profile.image
	user.profile.image.url
	```
	- We have to direct which directory the images will be stored when we upload new pictures for every user, we do this in the settings.py file
	- make a signal.py file so anytime we create a user, a profile is generated, and will be able to save the profile information 
	- Creating User/profile update forms
	- Make sure to update views.py file accordingly to make sure the new forms work as POST requests, and save appropriately. 
	- Resize photo on upload by going to models.py file and overwriting save method
	- Add profile image next to users post using home.html file

14. Implementing CRUD for Blog Posts
	- in our blog app directory, make a class based view for PostListView
	- update urls in blog dir
	- Do same for detail view to view indivisual posts
	- Now implement CRUD by using create, update, and delete views from djano documentation

15. Implementing Pagination 
	- run the following:
	```
	python manage.py shell
	from django.core.paginator import Paginator
	posts = ['1', '2', '3', '4', '5']
	p = Paginator(posts, 2)
	p.num_pages
	for page in p.page_range:
		print(page)
	p1 = p.page(1)
	p1.number
	p1.object_list
	p1.has_previous()
	p1.has_next()
	p1.next_page_number()
	```
	- Now we want to use that in blog -> views -> add paginator variable -> edit html

16. Additional Functionality
	- user post list view
	- password reset (allow app password access from gmail, make private env vars)


## How my file tree looks in the end
```
.
├── README.md
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── admin.cpython-37.pyc
│   │   ├── apps.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-37.pyc
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── static
│   │   └── blog
│   │       └── main.css
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── post_confirm_delete.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── user_posts.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── djangoProject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── media
│   ├── default.jpg
│   └── profile_pics
│       ├── danny.png
│       ├── pikachu.jpg
│       └── sefu_FeEuKhk.jpg
└── users
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── admin.cpython-37.pyc
    │   ├── apps.cpython-37.pyc
    │   ├── forms.cpython-37.pyc
    │   ├── models.cpython-37.pyc
    │   ├── signals.cpython-37.pyc
    │   └── views.cpython-37.pyc
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-37.pyc
    │       └── __init__.cpython-37.pyc
    ├── models.py
    ├── signals.py
    ├── templates
    │   └── users
    │       ├── login.html
    │       ├── logout.html
    │       ├── password_reset.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── profile.html
    │       └── register.html
    ├── tests.py
    └── views.py

18 directories, 67 files
```