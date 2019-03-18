from django.db import models

# Create your models here.
class Tracker(models.Model):
    baby = models.ForeignKey('babies.Babies', related_name='tracker', on_delete=models.CASCADE, null=False, default='')
    date = models.DateTimeField()
    weight = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        ordering = ('baby',)
