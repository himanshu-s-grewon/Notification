from django.db import models
from django.utils.translation import gettext_lazy as _


class Usertype(models.TextChoices):
    GENERAL = ("GENERAL", _("General"))
    BRANCH = ("BRANCH", _("Branch"))
    SUPPLIER = ("SUPPLIER", _("Supplier"))


class NotificationVerb(models.TextChoices):
    USER = ("USER", _("New User"))
    PRODUCT = ("PRODUCT", _("New Product"))
    ORDER = ("ORDER", _("New Order"))

