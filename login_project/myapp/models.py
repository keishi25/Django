from django.db import models


# Personal master data.
class Person(models.Model):
    # user_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=100, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=20, null=True)