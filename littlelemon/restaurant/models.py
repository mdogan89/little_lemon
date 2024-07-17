from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    guests = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        unique_together = ("name", "date")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title
