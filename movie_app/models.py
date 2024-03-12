from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    discripion = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=1, choices=[(i, i * '*') for i in range(6)])

    def __str__(self):
        return self.text