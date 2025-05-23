from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)  # We'll retain the IDs from users.json
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.URLField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
