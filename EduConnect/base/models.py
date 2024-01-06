from django.db import models
from django.contrib.auth.models import User   # Import User model from django.contrib.auth.models (built-in)        
# from django.db.models.deletion import CASCADE   # If room is deleted, delete all messages in that room


# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # If user is deleted, set host to null
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)  # If topic is deleted, set topic to null
    # participants =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']    # Order by updated and created fields in descending order


    def __self__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # If user is deleted, delete all messages from that user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)    # If room is deleted, delete all messages in that room
    body = models.TextField()   # Message body
    updated = models.DateTimeField(auto_now=True)   # When message was updated
    created = models.DateTimeField(auto_now_add=True)   # When message was created  

    def __str__(self):
        return self.body[:50]