# to-do-django

## Requirements Machine Setup 

### pyenv

Install the pyenv to manage multiple python versions. 

unix/macos:
https://github.com/pyenv/pyenv#unixmacos

windows:
https://github.com/pyenv/pyenv#windows

### python 3.10.7

Install and use python 3.10.7 to be able to run the project

```
pyenv install 3.10.7
pyenv global 3.10.7
```

## Running project

First clone the project running:
```
git clone git@github.com:eversonps/to-do-django.git
```

after clone, navegue ate o diretorio do projeto e instale o framework django:
```
pip install django djangorestframework
```

run the project migrations:
```
python manage.py migrate  
```

starting development server:
```
python3 manage.py runserver
```

now, check if project is running on http://127.0.0.1:8000/




