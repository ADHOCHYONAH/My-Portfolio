from django.db import models


# Create your models here.
class PORTFOLIOITEM(models.Model):
    email = models.EmailField(('email address'), unique=True, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone_no = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    def is_valid(self):
        pass
