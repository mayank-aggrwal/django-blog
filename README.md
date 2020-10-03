
# Djangolog

Djangolog is a blogging application built using the django framework in Python

## Features

1. User login
2. Creating articles
3. Editing existing articles
4. Comments on articles
5. Contact me form

## Installation

1. From the main working directory, run the below commands
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2. Set the username and password in settings.py file for sending mails
3. To start the server, run
    ```bash
    python manage.py runserver
    ```
4. Create a superuser to log in to django-admin
    ```bash
    python manage.py createsuperuser
    ```

## Additional instructions

### Install Python :
From [official website](https://www.python.org/downloads/)


### To check version of Python :
```bash
py --version
python --version
```

### Create a virtual environment :
```bash
py -m venv blog_app
```

### To activate virtual-environment :
```bash
.\blog_app\Scripts\activate
```

### To deactivate virtual-environment :
```bash
.\blog_app\Scripts\deactivate
```

### To install a package in virtual environment :
```bash
py -m pip install package_name
```

### To install django :
```bash
py -m pip install django
django --version
```

### While activating if terminal shows, "running scripts is disabled on this system"
There are 4 policy levels to choose from. From most secure to most insecure:
1. Restricted: No Powershell scripts can be run. This is the default setting.
2. AllSigned: Scripts can be run, but all must have a digital signature. Even if you wrote the script yourself on the local computer.
3. RemoteSigned: Locally-written scripts can be run. But scripts from outside (email, IM, Internet) must be signed by a trusted publisher.
4. Unrestricted: Any script will run. Regardless of who created them or whether they are signed. 

    To view the current systemwide Execution Policy setting :
    ```bash
    Get-ExecutionPolicy
    ```

    To set execution policy :
    ```bash
    Set-ExecutionPolicy remotesigned
    ```

### Touch alternative in windows powershell :
```bash
$null > file_name.cpp
```

### Configure GIT :
```bash
git config --global user.email "user_mail"
git config --global user.name "user_name"
```

###### NOTE: Make .gitignore file after initialising the GIT repository
<br>

### To run the application server :
```bash
python manage.py runserver
```

### For migrating the models to the database :
```bash
python manage.py makemigrations
python manage.py migrate
```

### While making a POST request through a form to the server, include :
```python
{% csrf_token %}
```

### To list all the branches in the git repository:
```bash
git branch -a
```

### To see branch graphs in git:
```bash
git log --graph --oneline --decorate --all
```

### To see all remotes
```bash
git remote -v
```

### To push all branches to remote repository
```bash
git push --all remote-origin
```

### To add a new remote to push changes to
```bash
git remote add new-remote-origin-name https://github.com/user_name/repo.git
```

### If you happen to delete db.sqlite3 file, run:
```bash
python manage.py migrate
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)