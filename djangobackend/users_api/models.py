from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin


class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None, **args):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email, **args)
		user.set_password(password)
		user.is_active = True
		user.save()
		return user
	
	def create_superuser(self, email, password=None, **args):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password, **args)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user
	

class AppUser(AbstractUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	username = models.CharField(max_length=50)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	objects = AppUserManager()
	def __str__(self):
		return self.username
	

class DentalProfile(models.Model):
	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	test_kit_id = models.CharField(max_length=32)
	title = models.CharField(max_length=128)
	description = models.TextField(null=True, blank=True)

