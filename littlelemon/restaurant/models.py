from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    guests = models.SmallIntegerField()
    date = models.DateTimeField()

    # class Meta:
    #     # unique_together = ("name", "date")

    def __str__(self):
        return f"{self.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(null=False, max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} : {str(self.price)}"

    def get_item(self):
        return f"{self.title} : {str(self.price)}"

    # class Meta:
    #     verbose_name = 'Menu'
    #     verbose_name_plural = 'Menu Items'
