from django.utils.translation import gettext_lazy as _


__version__ = '0.2.1'

GENDER_CHOICES = (
    ('u', _('undefined')),
    ('M', _('Male')),
    ('F', _('Female')),
)

LOOKFOR_CHOICES = (
    ('a', _('any')),
    ('M', _('Man')),
    ('F', _('Female')),
)
