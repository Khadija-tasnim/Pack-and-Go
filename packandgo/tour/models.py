from django.db import models

class TourDestinations(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TourImage(models.Model):
    tour = models.ForeignKey(TourDestinations, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tour_images/')

    def __str__(self):
        return f"Image for {self.tour.name}"
