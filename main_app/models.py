from django.db import models
from django.urls import reverse




class Accessory(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    def __str__(self):
        return f"A {self.name} {self.brand} {self.model}"

    def get_absolute_url(self):
        return reverse('accessories_detail', kwargs={'pk': self.id})
    

class Motorcycle(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'motorcycle_id': self.id})

class Mile(models.Model):
    date = models.DateField('Ride Date')
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_date_display()} on {self.date}"
        # get_<attribute name>_display()
    class Meta:
        ordering = ["date"]
class Photo(models.Model):
  url = models.CharField(max_length=200)
  motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE)
  def __str__(self):
      return f"Photo for motorcycle_id: {self.Motorcycle_id} @{self.url}" 
       
                