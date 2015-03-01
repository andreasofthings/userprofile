# user
python-social-auth application for django, packaged

.. image:: https://travis-ci.org/aneumeier/user.svg
    :target: https://travis-ci.org/aneumeier/user

.. image:: https://coveralls.io/repos/aneumeier/user/badge.svg?branch=master
  :target: https://coveralls.io/r/aneumeier/user?branch=master


Example Usage::
  from django.conf.urls import patterns, url, include
  urlpatterns = patterns(
    ''
    url('^user/', include('user.urls', namespace='user')),
  )
