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
### Celery, RabbitMQ, Redis and Flower
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
_Terminal 4_
```shell
docker run -it --rm --name redis -p 6379:6379 redis
```
***
### Stripe CLI
```shell
stripe login
stripe listen --forward-to localhost:8000/payment/webhook/
```
***
### Memchacked
```shell
docker pull memcached
docker run -it --rm --name memcached -p 11211:11211 memcached -m 64
```
### Covered chapters
* **Chapter 8**: Building an Online Shop
   * Creating an online shop project
   * Building a shopping cart
   * Registering customer orders
   * Asynchronous tasks

* **Chapter 9**: Managing Payments and Orders
   * Integrating a payment gateway
   * Exporting orders to CSV files
   * Extending the administration site with custom views
   * Generating PDF invoices dynamically

* **Chapter 10**: Extending Your Shop
  * Creating a coupon system
  * Building a recommendation engine

* **Chapter 11**: Adding Internationalization to Your Shop
  * Preparing your project for internationalization
  * Translating Python code
  * Translating templates
  * Rosetta
  * Fuzzy translations
  * URL patterns
  * Switching languages
  * django-parler
  * Format localization
  * django-localflavor

* **Chapter 12**: Building an E-Learning Platform
  * Setting up the e-learning project
  * Serving media files
  * Building the course models
  * Creating models for polymorphic content
  * Adding authentication views

* **Chapter 13**: Creating a Content Management System
  * Creating a CMS
  * Managing course modules and the contents

* **Chapter 14**: Rendering and Caching Content
  * Displaying courses
  * Adding student registration
  * Accessing the course contents
  * Using the cache framework

* **Chapter 15**: Building an API
  * Building a RESTful API

* **Chapter 16**: Building a Chat Server
  * Creating a chat application
  * Real-time Django with Channels
  * Installing Channels
  * Writing a consumer
  * Routing
  * Implementing the WebSocket client
  * Enabling a channel layer
  * Modifying the consumer to be fully asynchronous

***
### Chapter 8 - Additional resources
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

### Chapter 9 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter09)
- [Stripe website](https://www.stripe.com/)
- [Stripe Checkout documentation](https://stripe.com/docs/payments/checkout)
- [Creating a Stripe account](https://dashboard.stripe.com/register)
- [Stripe account settings](https://dashboard.stripe.com/settings/account)
- [Stripe Python library](https://github.com/stripe/stripe-python)
- [Stripe test API keys](https://dashboard.stripe.com/test/apikeys)
- [Stripe API keys documentation](https://stripe.com/docs/keys)
- [Stripe API version 2022-08-01 release notes](https://stripe.com/docs/upgrades#2022-08-01)
- [Stripe checkout session modes](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-mode)
- [Building absolute URIs with Django](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpRequest.build_absolute_uri)
- [Creating Stripe sessions](https://stripe.com/docs/api/checkout/sessions/create)
- [Stripe-supported currencies](https://stripe.com/docs/currencies)
- [Stripe Payments dashboard](https://dashboard.stripe.com/test/payments)
- [Credit cards for testing payments with Stripe](https://stripe.com/docs/testing)
- [Stripe webhooks](https://dashboard.stripe.com/test/webhooks)
- [Types of events sent by Stripe](https://stripe.com/docs/api/events/types)
- [Installing the Stripe CLI](https://stripe.com/docs/stripe-cli#install)
- [Latest Stripe CLI release](https://github.com/stripe/stripe-cli/releases/latest)
- [Generating CSV files with Django](https://docs.djangoproject.com/en/4.1/howto/outputting-csv/)
- [Django administration templates](https://github.com/django/django/tree/4.0/django/contrib/admin/templates/admin)
- [Outputting PDF files with ReportLab](https://docs.djangoproject.com/en/4.1/howto/outputting-pdf/)
- [Installing WeasyPrint](https://weasyprint.readthedocs.io/en/latest/install.html)
- [Static files for this chapter](https://github.com/PacktPublishing/Django-4-by-Example/tree/main/Chapter09/myshop/shop/static)

### Chapter 10 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter10)
- [Discounts for Stripe Checkout](https://stripe.com/docs/payments/checkout/discounts)
- [The Redis ZUNIONSTORE command](https://redis.io/commands/zunionstore/)

### Chapter 11 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter11)
- [List of valid language IDs](http://www.i18nguy.com/unicode/language-identifiers.html)
- [List of internationalization and localization settings](https://docs.djangoproject.com/en/4.1/ref/settings/#globalization-i18n-l10n)
- [Homebrew package manager](https://brew.sh/)
- [Installing gettext on Windows](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#gettext-on-windows)
- [Precompiled gettext binary installer for Windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)
- [Documentation about translations](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/)
- [Poedit translation file editor](https://poedit.net/)
- [Documentation for Django Rosetta](https://django-rosetta.readthedocs.io/)
- [The django-parler module’s compatibility with Django](https://django-parler.readthedocs.io/en/latest/compatibility.html)
- [Documentation for django-parler](https://django-parler.readthedocs.io/en/latest/)
- [Django formatting configuration for the Spanish locale](https://github.com/django/django/blob/stable/4.0.x/django/conf/locale/es/formats.py)
- [Django format localization](https://docs.djangoproject.com/en/4.1/topics/i18n/formatting/)
- [Documentation for django-localflavor](https://django-localflavor.readthedocs.io/en/latest/)

### Chapter 12 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter12)
- [Using Django fixtures for testing](https://docs.djangoproject.com/en/4.1/topics/testing/tools/#fixture-loading)
- [Data migrations](https://docs.djangoproject.com/en/4.1/topics/migrations/#data-migrations)
- [Creating custom model fields](https://docs.djangoproject.com/en/4.1/howto/custom-model-fields/)
- [Static directory for the e-learning project](https://github.com/PacktPublishing/Django-4-by-Example/tree/main/Chapter12/educa/courses/static)

### Chapter 13 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter13)
- [Django mixins documentation](https://docs.djangoproject.com/en/4.1/topics/class-based-views/mixins/)
- [Creating custom permissions](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-permissions)
- [Django formsets](https://docs.djangoproject.com/en/4.1/topics/forms/formsets/)
- [Django model formsets](https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#model-formsets)
- [HTML5 drag-and-drop API](https://www.w3schools.com/html/html5_draganddrop.asp)
- [HTML5 Sortable library documentation](https://github.com/lukasoppermann/html5sortable)
- [HTML5 Sortable library examples](https://lukasoppermann.github.io/html5sortable/)
- [django-braces documentation](https://django-braces.readthedocs.io/)

### Chapter 14 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter14)
- [django-embed-video documentation](https://django-embed-video.readthedocs.io/en/latest/)
- [Django’s cache framework documentation](https://docs.djangoproject.com/en/4.1/topics/cache/)
- [Memcached downloads](https://memcached.org/downloads)
- [Memcached official website](https://memcached.org)
- [Pymemcache 's source code](https://github.com/pinterest/pymemcache)
- [Django Redisboard’s source code](https://github.com/ionelmc/django-redisboard)

### Chapter 15 - Additional resources
- [Source code for this chapter](https://github.com/PacktPublishing/Django-4-by-example/tree/main/Chapter15)
- [REST framework website](https://www.django-rest-framework.org/)
- [REST framework settings](https://www.django-rest-framework.org/api-guide/settings/)
- [REST framework renderers](https://www.django-rest-framework.org/api-guide/renderers/)
- [REST framework parsers](https://www.django-rest-framework.org/api-guide/parsers/)
- [REST framework generic mixins and views](https://www.django-rest-framework.org/api-guide/generic-views/)
- [Download curl](https://curl.se/download.html)
- [Postman API platform](https://www.getpostman.com/)
- [REST framework serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [HTTP basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)
- [REST framework authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [REST framework permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [REST framework ViewSets](https://www.django-rest-framework.org/api-guide/viewsets/)
- [REST framework routers](https://www.django-rest-framework.org/api-guide/routers/)
- [Python Requests library documentation](https://requests.readthedocs.io/en/master/)
- [Authentication with the Requests library](https://requests.readthedocs.io/en/master/user/authentication/)
