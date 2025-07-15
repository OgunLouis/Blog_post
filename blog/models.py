from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #Timestamp when post is created.
    updated_at = models.DateTimeField(auto_now=True) #Updates whenever post is edited.

    def __str__(self):
        return f"{self.title} by {self.author}"

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    about = models.TextField()
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile | Age: {self.age} | About: {self.about[:30]}"
