from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    
    # Use ImageField for photo uploads
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    # Use URLField for social media links
    instagram_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    facebook_link = models.CharField(max_length=255)
    
    # Use DateTimeField for timestamps
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
