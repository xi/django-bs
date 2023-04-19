Bootstrap forms for Django
==========================

Bootstrap integration for django using [widget templates].

Motivation
----------

This library is meant to be a drop-in replacement for [django-bootstrap5]. See
below for a list of differences. I really like that library, but it is hard to
customize some things because everything is done in python functions. By using
widget templates, I hope this library is more flexible.

Installation
------------

Install with pip:

    pip install 'django-bs==4.*'  # for bootstrap 4
    pip install 'django-bs==5.*'  # for bootstrap 5

After that you have to add it to `INSTALLED_APPS`. You also need to make sure
that the correct `FORM_RENDERER` is selected and `django.forms` is in
`INSTALLED_APPS` (after `django_bs`). This is required so that widget
templates can be overwritten:

    INSTALLED_APPS = [
        …
        'django_bs',
        …
        'django.forms',
        …
    ]

    FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

Usage
-----

The following template tags are included in the `bootstrap` library:

-   `bootstrap_field {boundfield}` - Render a single field.
-   `bootstrap_form {form}` - Render errors and all fields for a form. The
    `<form>` element itself is not included.
-   `bootstrap_messages` - Render messages from `django.contrib.messages`.
-   `bootstrap_pagination {page}` - Render pagination. A `<nav>` element is not
    included.

Please refer to the source code for additional parameters.

Differences to django-bootstrap5
--------------------------------

-   Uses widget templates instead of custom renderers. IMHO this makes the code
    much easier to read and customize. A big downside is that I had to
    monkey-patch `BoundField.as_widget()` to include some information that
    would otherwise not be available in the widget templates.
-   Also overwrites the default form template in Django 4.0 and later so that
    `{{ form }}` does the right thing automatically.
-   Concentrates on forms fields and does therefore not include some other
    features.
-   Uses `.form-text.text-danger` instead of `.invalid-feedback` as it does not
    depend on DOM location. (see also [twbs/bootstrap\#29439])
-   Does not use `.is-valid` because I find it confusing with server-side
    rendering.
-   Does not include dismiss-buttons for alerts to avoid depending on
    JavaScript.
-   Non-field errors are styled as alerts.
-   Improved accessibility.
-   You will have to load bootstrap yourself.
-   No configuration.

[widget templates]: https://docs.djangoproject.com/en/stable/ref/forms/renderers/#overriding-built-in-widget-templates
[django-bootstrap5]: https://github.com/zostera/django-bootstrap5
[twbs/bootstrap\#29439]: https://github.com/twbs/bootstrap/issues/29439
