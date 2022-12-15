# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _

HELP_MESSAGES = {
    "slug": _("Site settings code name which indicate the settings section"),
    "name": _("Web application name"),
    "title": _("Web application title, (it used in SEO)"),
    "email": _("Web application contact email address"),
    "url": _("Web application URL"),
    "description": _("Description for the website. (it used in SEO)"),
    "keywords": _("Keywords indicate for the website, separated by (,). (it used in SEO)"),
    "logo": _("Web application logo image"),
    "phone": _("Web application phone number"),
    "manager_name": _("Manager full name"),
    "is_closed": _("Is web application open or close"),
    "close_message": _("Close message which will appear when close"),
    "can_assistants_login": _("Can assistants login to web application"),
    "can_bookkeepers_login": _("Can bookkeepers login to web application"),
    "facebook": _("Facebook URL"),
    "twitter": _("Twitter URL"),
    "youtube": _("Youtube channel URL"),
    "instagram": _("Instagram channel URL"),
}
