# my_site
### The essence of the created:
The **my_site** resource was created to do a homework called **Final Project**. 

The site is a mini-blog, which I plan to fill in the future with small articles about how I studied at the ItStep academy and, in fact, did my homework.

According to the task, the project includes technologies for storing data in the **database** (SQL) - **validation** of extreme cases so that users can not hack services - **tests**.

In the future, it is planned to develop the portfolio by adding new modules.

To start a project *(sample code is for windows, if you already have linux, you already know it;)* it must be cloned to a computer with the command
 
``git clone https://github.com/SergMagpie/my_site.git``

Then go to the folder my_site with the command

``cd my_syte``

Create a virtual environment with the command

``python -m venv venv_for_my_site``

Activate it with the command

``venv_for_my_site\Scripts\activate.bat``

Install the required packages with the command

``pip install requirements.txt``

Create a database with the command

''python manage.py migrate''

Create a user command

''python manage.py createsuperuser''

You can then run the project with the command

``python manage.py runserver``

In which case, please contact with me.
