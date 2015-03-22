# userprofile
python-social-auth application for django, packaged

.. image:: https://travis-ci.org/aneumeier/userprofile.svg
    :target: https://travis-ci.org/aneumeier/userprofile

.. image:: https://coveralls.io/repos/aneumeier/userprofile/badge.svg?branch=master
  :target: https://coveralls.io/r/aneumeier/userprofile?branch=master


Example Usage settings.py::
  INSTALLED_APPS = (
    ...
     'social.apps.django_app.default',
     'userprofile',
    ...
  )

Example Usage urls.py::
  from django.conf.urls import patterns, url, include
  urlpatterns = patterns(
    ''
    url('^user/', include('userprofile.urls', namespace='user')),
  )
