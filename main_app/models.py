from django.db import models
from django.urls import reverse

# Set up meal choices
MEALS = [
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
]

# Create your models here.
class Cat(models.Model):
  # define the fields/columns
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"