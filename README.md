Demo-Heroku
========

This is a simple demo to play with [Heroku](https://www.heroku.com/).

It is written in Python and relies in [Flask](http://flask.pocoo.org/). It is meant
to show a standard development lifecycle and deployment to Heroku.

Go ahead and clone this repository.

```
git clone https://github.com/magandrez/heroku-demo.git
```

Assuming [virtual environment](https://virtualenv.readthedocs.org/en/latest/) for Python is installed and active. Install required packages with pip:

```
pip install flask
pip install gunicorn
```

Freeze the requirements into a ```requirements.txt``` file with pip:

```
pip freeze > requirements.txt
```

Login into Heroku, create project and push to publish:

```
heroku login
heroku apps:create myheroku-demo
git push heroku master
```

And you are ready to hack away.

Requirements
------------
- Python >=2.7
- Virtualenv
- [Heroku toolbelt](https://toolbelt.heroku.com/)
