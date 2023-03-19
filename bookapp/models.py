from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  bookimage = models.ImageField(upload_to='', blank=True, null=True)
  date = models.DateTimeField()

  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ["date"]
