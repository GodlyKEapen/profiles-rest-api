from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
#"""" Respents a "user profile" inside our system."""

    def create_user(self, email, name, password=None):
        #"""creates a new user profile object."""

        if not email:
            raise ValueError("Users must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

        def cerate_superuser(self, email, password):
            #"""creates and saves a new superuser with given details."""

            user = self.create_user(email, name, password)

            user.is_superuser = true
            usre.is_staff = true

            user.save(using=self._db)

            return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # """Respents a "User Profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REWUIRED_FIELDS = ["name"]

    def get_full_name(self):
    #    """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        # Used to get a users get_short_name.

        return self.name

    def _str_(self):
     # Django uses this when it needs to convert the objects to a string

     return self.email
