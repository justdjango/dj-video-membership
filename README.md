<p align="center">
  <p align="center">
    <a href="https://justdjango.com/?utm_source=github&utm_medium=logo" target="_blank">
      <img src="https://assets.justdjango.com/static/branding/logo.svg" alt="JustDjango" height="72">
    </a>
  </p>
  <p align="center">
    The Definitive Django Learning Platform.
  </p>
</p>

# Django Video Membership Website

This is a video membership website built with Django.

This project was bootstrapped with [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django/)

![https://github.com/pydanny/cookiecutter-django/](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)
![https://github.com/ambv/black](https://img.shields.io/badge/code%20style-black-000000.svg)

### Learn Django

This project is part of a course on [JustDjango](https://learn.justdjango.com). If you want to learn how to become a professional Django developer, consider signing up for access to our courses.

### Getting started

To have the project up and running, create a .env file in the root of this project and enter the environment variables according to the `.template.env` file.

You will need to set this environment variable so that it reads the `.env` file:

```
export DJANGO_READ_DOT_ENV_FILE=True
```

### Type checks

Running type checks with mypy:

```
mypy djvideomem
```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

```
coverage run -m pytest
coverage html
open htmlcov/index.html
```

### Running tests with py.test

```
pytest
```

### Celery

```bash
celery -A config.celery_app worker -l info
```

Make sure to have redis running with

```
redis-server
```

---

<div align="center">

<i>Other places you can find us:</i><br>

<a href="https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ" target="_blank"><img src="https://img.shields.io/badge/YouTube-%23E4405F.svg?&style=flat-square&logo=youtube&logoColor=white" alt="YouTube"></a>
<a href="https://www.twitter.com/justdjangocode" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231877F2.svg?&style=flat-square&logo=twitter&logoColor=white" alt="Twitter"></a>

</div>
