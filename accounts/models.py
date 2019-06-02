from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r"^\+?98?\d{10,10}$", message="شماره را به صورت +98123456789 وارد کنید"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    person_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    def natural_key(self):
        return self.phone_number

    def get_short_name(self):
        return self.person_name

    def get_full_name(self):
        return self.person_name
