5.4.0 (2025-11-25)
------------------

-   rename `form_group_class` to `wrapper_class` to align with
    django-bootstrap5. `form_group_class` is still supported, but deprecated.


5.3.0 (2025-09-15)
------------------

-   support `form.required_css_class` (added to the label like in django, but
    different from django-bootstrap5)
-   breaking: it is no longer possible to skip a label completely
-   fix: `show_label=False` create a visually hidden label


5.2.1 (2025-09-03)
------------------

-   fix missing templatetags in package


5.2.0 (2025-03-03)
------------------

-   switch to pyproject.toml
-   add support for Django 5.x


5.1.0 (2023-04-18)
------------------

-   add support for Django 4.x
-   fix rendering of hidden fields in `bootstrap_form`
-   overwrite the default form template so that `{{ form }}` will produce the
    same output as `{% bootstrap_form form %}` (starting with Django 4.0)
-   starting with Django 4.0, make use of `widget.use_fieldset`
-   use same font size for `<legend>` as for `<label>`
-   work around extensive spacing between legend and multiwidget


5.0.0 (unreleased)
------------------

-   adapt to bootstrap 5


4.0.0 (unreleased)
------------------

-   use underscore in app name
-   help text and error inside form-check
-   use fieldsets where appropriate (django #32338)
-   change versioning to align with bootstrap
-   change package name to "django-bs" and tag library name to "bootstrap".


0.0.4 (2021-01-25)
------------------

-   clearable file input
    -   fix line break
    -   fix disable checkbox when disabled (django #31536)
    -   fix use bootstrap styling


0.0.3 (2020-06-17)
------------------

-   Fix `radio_option` include path


0.0.2 (2020-01-26)
------------------

-   Fix some infos in setup.py


0.0.1 (2020-01-26)
------------------

-   Initial release
