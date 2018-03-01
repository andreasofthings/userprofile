#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
urly.py to allow tests in travis-ci
"""

from django.conf.urls import url, include

urlpatterns = [
    '',
    url('^user/', include('userprofile.urls', namespace='user')),
    url('', include('social.apps.django_app.urls', namespace='social'))
]
