from django.db                  import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Username obligatorio')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    id          = models.BigAutoField(primary_key=True)
    username    = models.CharField('Username', unique=True, max_length=20)
    password    = models.CharField('Password', max_length=256)
    nombre      = models.CharField('Nombre', max_length=50)
    email       = models.EmailField('Email', max_length=100, unique=True)
    rol_jardinero    = models.BooleanField('Rol', help_text="Si su rol es Jardinero True, si es un usuario corriente False", null=False )
    descripcion      = models.CharField('Descripcion', max_length=256, null=True)
    ciudad           = models.CharField('Ciudad', max_length=30, null=True)
    telefono         = models.CharField('Telefono', max_length=20, null=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'
