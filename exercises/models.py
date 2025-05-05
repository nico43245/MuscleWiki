
from django.db import models

difficulty_choices = [
        ('easy', 'Ușor'),
        ('medium', 'Mediu'),
        ('hard', 'Dificil'),
    ]



class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    video_url = models.URLField()
    description = models.TextField()
    muscle_group = models.ForeignKey(
        MuscleGroup,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    def __str__(self):
        return self.name
