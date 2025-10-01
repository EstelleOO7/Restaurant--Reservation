from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(20)])
   special_requests_comments = models.CharField(max_length=1000)
   date = models.DateTimeField()
   phone_number = models.CharField(max_length=15)
   email = models.EmailField(max_length=254)
   reservation_active = models.BooleanField(default=True)  
   assigned_date = models.DateTimeField(null=True, blank=True)
   number_of_hours = models.IntegerField(blank=True, null=True)
   
   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Menu(models.Model):
   name = models.CharField(max_length=300)
   price = models.IntegerField()
   description = models.TextField(null=True, blank=True)
   

   def __str__(self):
      return self.name
   
   def get_image_url(self):
      """Return image URL based on menu item name"""
      image_name = self.name.lower().replace(' ', '_').replace("'", "") + '.jpg'
      return f'/static/img/menu_items/{image_name}'
   
   def get_image_filename(self):
      """Return just the image filename"""
      return self.name.lower().replace(' ', '_').replace("'", "") + '.jpg'