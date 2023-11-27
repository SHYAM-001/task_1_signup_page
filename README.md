# Hi, I'm Shyam K S! 👋


# task_1_signup_page

This Django-based web application provides a user-friendly platform for patients and doctors to register, login, and manage their profiles.

## Features:
### Patient Signup:

Register as a patient with personal details, address, and profile picture.
### Doctor Signup:

Register as a doctor with specialization, experience, contact details, and profile picture.
### Login:

Secure login system for both patients and doctors.
### Home Page:

Dynamic home page displaying personalized content based on the user's role (patient or doctor).


## Screenshots

### Home page
![Screenshot 2023-11-27 203039](https://github.com/SHYAM-001/task_1_signup_page/assets/103324177/367da390-b646-4cad-95ec-aa50a0b54c63)

### Login

![Screenshot 2023-11-27 203141](https://github.com/SHYAM-001/task_1_signup_page/assets/103324177/dd3a7e75-8e9e-4a5a-bd65-589912fc0ee4)

### Registeration

![Screenshot 2023-11-27 203225](https://github.com/SHYAM-001/task_1_signup_page/assets/103324177/80884ddd-7342-4d71-8f6e-38e27f2abf2f)

## Installation

Install my-project with `git clone `

##### Get started!

```bash
   create a folder in the name you needed `your folder name`
```
```bash
  git clone https://github.com/SHYAM-001/task_1_signup_page.git
```
    
## Environment Variables

To run this project, you will need to run the virtual Environment file `myVenv`

```bash
   source myVenv/Scripts/activate
```
If your system doesn't have the virtual Environment then,

```bash
   pip install venv
```


## To Run the project

After cloning and running `myVenv` 

Install django in the virtual environment

```bash
  pip install django
```
```bash
  pip install pillow
```
```bash
  pip install mysqlclient
```

Go to the project directory

```bash
  cd internship
```
start the database to run

```bash
   python manage.py makemigrations
```
```bash
   python manage.py migrate
```

After migration to manage the database create a superuser

```bash
   python manage.py createsuperuser
```

Start the server

```bash
  python manage.py runserver
```


## Authors

- [@SHYAM-001](https://www.github.com/SHYAM-001)
