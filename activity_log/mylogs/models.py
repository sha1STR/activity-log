from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Activity(models.Model):
  activity_name = models.CharField(max_length=64)
  start_date = models.DateTimeField("Start Date", default=timezone.now())
  end_date = models.DateTimeField("End Date", null=True)


  def __tuple__(self):
    return (self.activity_name, self.start_date, self.end_date)