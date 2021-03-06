from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.utils import timezone

class MyMgr(BaseUserManager):
    def create_user(self, email, area_of_interest="", password=None):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email,
                          joined=now, is_active=True, is_admin=False,
                          last_login=now)

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password, area_of_interest=""):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email,
                          joined=now, is_active=True, is_admin=True,
                          last_login=now)

        user.set_password(password)
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser):
    """
    Custom user class.
    """
    objects = MyMgr()
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    area_of_interest = models.CharField(max_length=50)  

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __unicode__(self):
        return self.email
    
