from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=100,null=True,blank=True)
    salary = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name,self.user.last_name)

@receiver(post_save,sender=User)
def user_is_created(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

        """ Django Signals : You can send the signals and you can receive the signals, that means if you want to do some
activity. Django itself provides an inbuilt signals.
After user you want to Profile automatically."""