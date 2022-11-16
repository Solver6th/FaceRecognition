from django.db import models

class Face(models.Model):
    image = models.ImageField(upload_to = "images/", null=True, blank=True)

    def __str__(self):
        return "face"