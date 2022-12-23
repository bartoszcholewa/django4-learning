# Django 4 by Example - Antonio Melé [packt] 2022
***
Repository is a continuation of [django3-learning](https://github.com/bartoszcholewa/django3-learning)
based on book of Antonio Melé - Django 3 By Example.
***
### Requirements
Project is based on **Python 3.10.*** and **Django 4.1.0**

All required packages are in `requirements.txt`
```shell
pip install -r requirements.txt
```
Add new package to `requirements.in` and compile new file by
```shell
pip-compile
```
To add and install new package run
```shell
pip-compile && pip-sync
```
***
### Pre-commit hooks
To add new pre-commit hook, edit `.pre-commit-config.yaml`

Then install new hooks by
```shell
pre-commit install
```
and check if everythin passes by
```shell
pre-commit run --all-files
```
***
### Celery, RabbitMQ and Flower
_Terminal 1_
```shell
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
```
_Termina 2_
```shell
celery -A myshop worker -l info
```
_Terminal 3_
```shell
celery -A myshop flower
```
***
### Covered chapters
1. Chapter 8: Building an Online Shop
   * Creating an online shop project
   * Building a shopping cart
   * Registering customer orders
   * Asynchronous tasks

Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter08)
- [Static files for the project](https://github.com/PacktPublishing/Django-4-by-Example/tree/main/Chapter08/myshop/shop/static)
- [Django session settings](https://docs.djangoproject.com/en/4.1/ref/settings/#sessions)
- [Django built-in context processors](https://docs.djangoproject.com/en/4.1/ref/templates/api/#built-in-template-context-processors)
- [Information about RequestContext](https://docs.djangoproject.com/en/4.1/ref/templates/api/#django.template.RequestContext)
- [Celery documentation](https://docs.celeryq.dev/en/stable/index.html)
- [Introduction to Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
- [Official RabbitMQ Docker image](https://hub.docker.com/_/rabbitmq)
- [RabbitMQ installation instructions](https://www.rabbitmq.com/download.html)
- [Flower documentation](https://flower.readthedocs.io/)
