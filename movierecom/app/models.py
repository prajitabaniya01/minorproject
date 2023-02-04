from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
# 'xHTwM2nLXmsRBl1T16WSDv-CWDsAQAyWluR_RTSADTY'

class Movie(models.Model):
    movie_id=models.IntegerField()
    title = models.CharField(max_length=200)
    overview=models.CharField(max_length=1000)
    genres = models.CharField(max_length=200)
    casts = models.CharField(max_length = 200)
    crew = models.CharField(max_length=50)
    tags = models.CharField(max_length=500)
    # poster = models.ImageField(upload_to='poster')
    # description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Myrating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=0, validators=[MaxValueValidator(5),
                               MinValueValidator(0)])


class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # watch = models.BooleanField(default=False)
