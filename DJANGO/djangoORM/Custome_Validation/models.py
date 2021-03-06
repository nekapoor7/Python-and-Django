from django.db import models
from django.core.exceptions import ValidationError

"""Creating a Validator Function"""

def validate_geeks_mail(value):
    if '@gmail.com' in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")


# Create your models here.

class GeeksModel(models.Model):
    geeks_mail = models.CharField(max_length=200,validators=[validate_geeks_mail])

