from django.db import models

class Type(models.Model):
  LARGE = "large"
  MEDIUM = "medium"
  MINI = "mini"
  SIZE_CHOICES = [
    (LARGE,"large"),
    (MEDIUM,"medium"),
    (MINI,"mini")
  ]
  WHITE = "white"
  BLACK = "black"
  COLOR_CHOICES = [
    (WHITE,"white"),
    (BLACK,"balck")
  ]
  item = models.CharField(max_length=255)
  size = models.CharField(
    max_length=6,
    choices = SIZE_CHOICES,
    default = MEDIUM,
  )
  price = models.IntegerField(null=True)
  color = models.CharField(
    max_length=5,
    choices = COLOR_CHOICES,
    default = BLACK,
  )
  sajin =models.ImageField(upload_to = 'images/', null=True)
  def __str__(self):
    return self.item