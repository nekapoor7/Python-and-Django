from django.db import models

# Create your models here.


class GeeksModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to= "C:/Users/nekapoor/Pictures/Saved Pictures")

    def __str__(self):
        self.title