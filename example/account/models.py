from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('У пользователя обязательно должен быть e-mail')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email   , password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=255,
        unique=True,
    )
    company_name = models.CharField(
    'Наименование компании',
    max_length=30,
    blank=True
    )
    phone = models.CharField(
    'Номер телефона',
    max_length=11,
    blank=True
    )
    first_name = models.CharField(
    'Фамилия',
    max_length=15,
    null=True,
    blank=True
    )
    last_name = models.CharField(
    'Имя',
    max_length=15,
    null=True,
    blank=True
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        self.first_letter = self.email[0]
        super().save()
