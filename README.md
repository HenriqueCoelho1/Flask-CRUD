# Python CRUD Challenge

### Challenge made by a friend

This was developed using Flask(Python Framework) on a Linux computer running the [Pop_OS!](https://pop.system76.com/) distro.

### About the Project

This software contains a User CRUD(Create, Read, Update, Delete).

The student can only have one username, one full name, and one email with the minimum of 11 characters and CPF(Cadastro de Pessoa Física).

### Requirements:

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)
- [PostgreSQL](https://www.postgresql.org/) (on local machine running on port 5432)
- [Git](https://git-scm.com/)

## Running project:

#### Creating database

1 - Check if your PostgreSQL is running on your computer

```sh
ss -tulpn | grep 5432
service postgresql status
```

#### Serving App

1 - We need to clone and grab all the dependencies:

```sh
git clone https://github.com/HenriqueCoelho1/Flask-CRUD.git
cd Flask-CRUD
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - On your backend folder run:

```sh
python3
```

and type:

```sh
from app import db
db.create_all()
```

Now we need to activate the the app.py, on your backend folder run:

```sh
export FLASK_APP=app.py
```

and then run:

```sh
flask run
```

### Happy hacking!

### Made with ♥ by [HenriqueCoelho1](https://br.linkedin.com/in/alleson-henrique-coelho-barbosa-19151a213)
