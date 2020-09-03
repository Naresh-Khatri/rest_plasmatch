from django.db import models


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, age, gender, phone_no, city, password=None):
        if not email:
            raise ValueError("user must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                    age=age, gender=gender, phone_no=phone_no, city=city)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, age, gender, phone_no, city, password):
        user = self.create_user(email, first_name, last_name, age, gender, phone_no, city, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(max_length=255, unique=True)
    first_name  = models.CharField(max_length=255, default='')
    last_name   = models.CharField(max_length=255, default='')
    age         = models.IntegerField(default=10)
    gender      = models.CharField(max_length=1,default='M')
    phone_no    = models.CharField(max_length=20, default='')
    city        = models.CharField(max_length=50, default= 'New Delhi')

    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects     = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age', 'gender', 'phone_no', 'city']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class DonorProfile(models.Model):
    email       = models.EmailField(max_length=255, unique=True, default='')
    first_name  = models.CharField(max_length=255, default='')
    last_name   = models.CharField(max_length=255, default='')
    dob         = models.CharField(max_length=15, default='')
    age         = models.IntegerField(default=10)
    gender      = models.CharField(max_length=1,default='M')
    phone_no    = models.CharField(max_length=20, default='')
    city        = models.CharField(max_length=50, default= 'New Delhi')
    lat         = models.CharField(max_length=20, default='')
    lng         = models.CharField(max_length=20, default='')

    diabetes            = models.BooleanField(default=False)
    lung               = models.BooleanField(default=False)
    kidney              = models.BooleanField(default=False)
    high_bp             = models.BooleanField(default=False)
    liver               = models.BooleanField(default=False)

    have_aadhar         = models.BooleanField(default=True)
    blood_type          = models.CharField(max_length=3)
    drinks_14           = models.BooleanField(default=False)
    discharge_report    = models.BooleanField(default=True)
    neg_2weeks          = models.BooleanField(default=True)


class PatientProfile(models.Model):
    email       = models.EmailField(max_length=255, unique=True, default='')
    first_name  = models.CharField(max_length=255, default='')
    last_name   = models.CharField(max_length=255, default='')
    dob         = models.CharField(max_length=15, default='')
    age         = models.IntegerField(default=10)
    gender      = models.CharField(max_length=1,default='M')
    phone_no    = models.CharField(max_length=20, default='')
    city        = models.CharField(max_length=50, default= 'New Delhi')
    lat         = models.CharField(max_length=20, default='')
    lng         = models.CharField(max_length=20, default='')

    hospital_name       = models.CharField(max_length=255)
    blood_type          = models.CharField(max_length=3)
    case_sheet_form     = models.BooleanField(default=True)

class Message(models.Model):
    name        = models.CharField(max_length=50, default='')
    email       = models.EmailField(max_length=255, default='')
    message    = models.CharField(max_length=1024)
