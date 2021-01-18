from django.db import models
from django.contrib.auth.models import User

class housing_data(models.Model): # should I put in blank=True, null=True
    user = models.ManyToManyField('users_app.CustomUser', blank=True)
    # created = models.DateField(auto_now_add=True)
    updated = models.DateField()
    projectName = models.CharField(max_length=100)
    management = models.CharField(max_length=100)
    zipCode = models.ForeignKey('neighborhood_data', on_delete=models.CASCADE)
    xCoord = models.FloatField(blank=True, null=True)                       # FUTURE DATA
    yCoord = models.FloatField(blank=True, null=True)                       # FUTURE DATA
    neighborhood = models.CharField(max_length=20, blank=True, null=True)   # FUTURE DATA
    address = models.CharField(max_length=100)
    contactPhone = models.CharField(max_length=12)
    totalUnits = models.IntegerField(blank=True, null=True)
    singleRoom = models.IntegerField(blank=True, null=True)
    studio = models.IntegerField(blank=True, null=True)
    oneBedroom = models.IntegerField(blank=True, null=True)
    twoBedroom = models.IntegerField(blank=True, null=True)
    threeBedroom = models.IntegerField(blank=True, null=True)
    fourBedroom = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.projectName
    
    class Meta:
        ordering = ['projectName']

class neighborhood_data(models.Model):
    zipCode = models.CharField(max_length=5, primary_key=True)
    safetyRank = models.IntegerField(blank=True, null=True)
    crimeIndex = models.FloatField()
    crimeCount = models.FloatField()
    crimeRatio = models.FloatField()
    neighborhood = models.CharField(max_length=20, blank=True, null=True)   # FUTURE DATA
    quadrant = models.CharField(max_length=10, blank=True, null=True)       # FUTURE DATA     
    avgRent = models.FloatField(blank=True, null=True)                      # FUTURE DATA
    rentLow = models.FloatField(blank=True, null=True)                      # FUTURE DATA
    rentHigh = models.FloatField(blank=True, null=True)                     # FUTURE DATA
    walkIndex = models.FloatField(blank=True, null=True)                    # FUTURE DATA
    violenceIndex = models.FloatField(blank=True, null=True)                # FUTURE DATA   
    crimeTime = models.CharField(max_length=2, blank=True, null=True)       # FUTURE DATA (AM or PM)
    avgHomeValue = models.FloatField(blank=True, null=True)                 # FUTURE DATA

    def __str__(self):
            return self.zipCode


















# Example 1:


# from django.db import models
# from django.contrib.auth.models import User

# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


# Example 2:


# from django.db import models
# from django.urls import reverse

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     caption = models.CharField(max_length=500)
#     photo = models.ImageField(upload_to="images/")

#     def get_absolute_url(self):
#         return reverse('instaface:detail', args=(self.id,))

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['-created']


# Example 3:
