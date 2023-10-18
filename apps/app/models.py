from django.db import models

class Plane(models.Model):

    name = models.CharField(max_length=100)
    characterisrics = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Airline(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateField(blank=True, null=True)
    planes = models.ManyToManyField(Plane, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Flight(models.Model):

    From = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, blank=True, null=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, blank=True, null=True)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.From}'
