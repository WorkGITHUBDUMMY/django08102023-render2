from django.db import models

# Create your models here.

class GoodMorning(models.Model):
    AMPM = (
        ('am', 'AM'),
        ('pm', 'PM'),
    )

    time_hour = models.IntegerField(null=True, blank=True)
    am_pm = models.CharField(max_length=10, choices=AMPM)

    def __str__(self):
        return str(self.id)+'-'+str(self.time_hour)+' '+self.am_pm