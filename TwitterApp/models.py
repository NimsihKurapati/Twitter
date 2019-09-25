from django.db import models
import uuid
from datetime import datetime
# Create your models here.
class T_user(models.Model):
    user_name = models.CharField(max_length=20)
    user_image = models.ImageField(default="NULL",upload_to='profile')
    user_email = models.EmailField()

    def __str__(self):
        return self.user_name

class Tweet(models.Model):
    user = models.CharField(max_length=20)
    original = models.CharField(max_length=20)
    content = models.TextField(max_length=270)
    comment = models.TextField(max_length=270,blank=True,null=True)
    date_time = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length = 30)
    uuid = models.UUIDField(default=uuid.uuid4, unique = True)
    RT = models.BooleanField(default=False)

    def __str__(self):
        return self.content