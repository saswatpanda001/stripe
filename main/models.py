


from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone




class Device(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name



class Plans(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    price_m = models.FloatField(blank=True,null=True)
    price_y = models.FloatField(blank=True,null=True)
    device = models.ManyToManyField(Device,blank=True,null=True)
    resolution = models.CharField(max_length=100,blank=True,null=True)
    video_quality = models.CharField(max_length=100,blank=True,null=True)
    active_screens = models.IntegerField(blank=True,null=True)
    
    
    def __str__(self):
        return self.name
    



class UserSubscription(models.Model):
    username = models.CharField(max_length=200,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    plan_status = models.BooleanField(blank=True,null=True)
    started = models.DateTimeField(default=timezone.now,blank=True,null=True)
    plan = models.ForeignKey(Plans,on_delete=models.CASCADE,blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    end =  models.DateTimeField(default=timezone.now,blank=True,null=True)


    def __str__(self):
        return self.username
    






