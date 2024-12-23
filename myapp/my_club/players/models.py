from django.db import models

class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.IntegerField(null=True)
    date_joined = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, Age: {self.age}"  # This is what will be displayed in the admin panel