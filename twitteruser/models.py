from django.db import models
from django.contrib.auth.models import AbstractUser


# https://stackoverflow.com/questions/16613013/model-self-dependency-one-to-many-field-implementation/16614136#16614136
class TwitterUser(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False)
