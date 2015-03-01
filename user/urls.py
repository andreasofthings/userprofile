from django.conf.urls import patterns, url

from userprofile.views import Home, Login, Logout, RequireEmail

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^require-email/$', RequireEmail.as_view(), name='require_email'),
)
