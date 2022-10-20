from django.db import models
from django.contrib.auth import models as auth_models
from api.models import Menu
from multiselectfield import MultiSelectField
# Create your models here.


class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have an first name")
        if not last_name:
            raise ValueError("User must have an last name")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email",
                              max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

DELIVERY_CHOICES = (
    (1, 'Preparing'),
    (2, 'In Route'),
    (3, 'Delivered'),
)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    delivery_status = MultiSelectField(
        max_length=10,
        max_choices=1,
        choices=DELIVERY_CHOICES,
        default=DELIVERY_CHOICES[0][0]
    )
    general_address = models.CharField(max_length=255,default="In store")
    specific_address = models.CharField(max_length=255,default="In store")
    zip_code = models.CharField(max_length=255,default="In store")

    def __str__(self):
        return self.item.name
