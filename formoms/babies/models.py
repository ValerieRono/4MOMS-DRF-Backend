from django.db import models
from users.models import User

# Create your models here.
class Babies(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    birth_date = models.DateField()
    weight_at_birth = models.IntegerField()
    height_at_birth = models.IntegerField()
    parent = models.ForeignKey('users.User', related_name='babies', on_delete=models.CASCADE, null=False, default='')

    class Meta:
        ordering = ('name',)