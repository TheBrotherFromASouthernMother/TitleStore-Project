from django.db import models

# Create your models here.
class people(models.Model):
    id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=200)
    age = models.IntegerField()
    def __str__(self):
        return self.person_name
