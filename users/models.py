from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from soins.models import SoinsSelect
from django.utils.timezone import now


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, story, name, forename, historique, adress1, adress2,
                     dateNaiss, fidelity, phone):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            story=story,
            name=name,
            forename=forename,
            historique=historique,
            adress1=adress1,
            adress2=adress2,
            dateNaiss=dateNaiss,
            fidelity=fidelity,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, story, name, forename, historique, adress1, adress2, dateNaiss, fidelity,
                    phone):
        return self._create_user(email, password, False, False, story, name, forename, historique, adress1, adress2,
                                 dateNaiss, fidelity, phone)

    def create_superuser(self, email, password, name: '', forename='', adress1='', adress2='', dateNaiss='', phone='',
                         story='', historique='', fidelity=0):
        user = self._create_user(email, password, True, True, story, name, forename, historique, adress1, adress2,
                                 dateNaiss, fidelity, phone)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, blank=False)
    name = models.CharField(max_length=254, null=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    story = models.TextField(blank=True)
    forename = models.CharField(max_length=254, null=True, blank=False)
    adress1 = models.CharField(max_length=254, null=True, blank=False)
    adress2 = models.CharField(max_length=254, null=True, blank=False)
    dateNaiss = models.DateField(default=now, null=True, blank=False)
    fidelity = models.IntegerField(default=0, null=True, blank=True, editable=True)
    phone = models.CharField(max_length=16, null=True, blank=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'forename', 'adress1', 'adress2', 'dateNaiss', 'phone']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


class SoinsList(models.Model):
    soin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Soins')
    liste = models.CharField(blank=True, max_length=254)
    Date = models.DateField(null=True, blank=True)
    isAccepted = models.BooleanField(null=True, blank=True, default=False)


class Historique(models.Model):
    historique = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Historique')
    HistoriqueDesSoins = models.CharField(blank=True, max_length=254)
    Date = models.DateTimeField(null=True, blank=True)


class Dispo(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Admin')
    id = models.AutoField(primary_key=True)
    Date = models.DateField(null=True, blank=True)
