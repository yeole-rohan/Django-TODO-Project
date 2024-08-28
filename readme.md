# Django TODO App

A simple TODO application built with Django for beginners. This project demonstrates basic CRUD operations, form handling, and integration with Bootstrap.

## Features

- Create, update, and delete TODO items.
- Move TODO items around on the window.
- Move items to the bin.
- Simple UI with Bootstrap for better user experience.

## Prerequisites

- Python 3.x
- Django 4.x
- Git
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yeole-rohan/Django-TODO-Project.git
cd Django-TODO-Project
```
## Create a Virtual Environment and  It

```bash
python -m venv env
# Windows
env\Scripts\activate
# MacOS/Linux
source env/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Set Up the Database

Run the following commands to apply migrations and set up the database:

```bash
python manage.py migrate 
```

## Create a Superuser (for Admin Access)

```bash
python manage.py createsuperuser
```

## Run the Application

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser to view the app.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions, issues, and feature requests are welcome!