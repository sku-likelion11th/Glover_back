from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=100)
    full_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.full_name
    
    
class Stamp(models.Model):
    event_name = models.CharField(max_length=200)
    event_info = models.TextField()
    event_start = models.DateField()
    event_end = models.DateField()
    before_image = models.ImageField(upload_to='before_images/')
    after_image = models.ImageField(upload_to='after_images/')
    
    def __str__(self):
        return self.event_name
    
    
class UserProfile(models.Model):
    user_name = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    stamps = models.ManyToManyField(Stamp, through='StampRecord')
    
    def __str__(self):
        return self.user_name
    
    
class StampRecord(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE)
    is_collected = models.BooleanField(default=False)
    
    