from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=20, unique=True)
    password = models.CharField('Password', max_length=256)
    nombre = models.CharField('Name', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    email = models.EmailField('Email', max_length=100)
    tipo_documento = models.CharField('Tipo de documento', max_length=50)
    numero_documento = models.CharField('Numero de documento', max_length=50)
    direccion = models.CharField('Direccion', max_length=100)
    telefono = models.CharField('Telefono', max_length=50)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    USERNAME_FIELD = 'username'
