from django.db import models
from datetime import time

# Define Room model
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor}"

# Define Meeting model (singular)
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))  # Default start time at 9 AM
    duration = models.IntegerField(default=1)  # Duration in hours
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Link to Room model

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
