from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from apps.utils.constants import *


class UserManager(BaseUserManager):
    def create_user(self, username, email, nickname, password=None):
        if not email:
            raise ValueError('must have an email address.')
        usuario = self.model(email=self.normalize_email(email), username=username, nickname=nickname)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, email, nickname, password):
        usuario = self.create_user(email=email, username=username, password=password, nickname=nickname)
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario


CHOICE_GENDER = (
    (GenderType.MALE.value, "Male"),
    (GenderType.FEMALE.value, "Female"),
    (GenderType.OTHER.value, "Other"),
)

CHOICE_STATUS = (
    (UserStatus.ACTIVE.value, "Activated"),
    (UserStatus.POLICY_VIOLATION.value, "Policy violation"),
)


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=255, unique=True, default=None)
    full_name = models.CharField(max_length=255, default=None)
    phone = models.IntegerField(default=None)
    gender = models.IntegerField(choices=CHOICE_GENDER, default=GenderType.MALE.value)
    birthday = models.DateField(blank=True, null=True)
    rank = models.FloatField(default=None)
    identification = models.IntegerField(default=None)
    role_name = models.CharField(max_length=255, default=None)
    role_description = models.CharField(max_length=255, default=None)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_sub_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return '{}-{}'.format(self.id, self.username)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_admin_user(self):
        "Is the user a member of super admin or sub admin?"
        return self.is_admin or self.is_sub_admin


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'token'

    def __str__(self):
        return "{} - {} - {}".format(self.id, self.user_id, self.token)
