from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vacancy(models.Model):
    author = models.ForeignKey(User, related_name="vacancy_author", on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
#    author.is_staff = True
