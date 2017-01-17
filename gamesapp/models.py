from django.db import models
from django.utils import timezone


class Game(models.Model):
    game_id = models.CharField(unique=True)
    name = models.TextField()
    description = models.TextField()
    genre = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return self.name


class HighScore(models.Model):
    user_id = models.TextField()
    game_id = models.TextField()
    score = models.IntegerField(blank=False, null=True)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return 'user_id: ' + self.user_id + ' | game_id: ' + self.game_id + ' | score: ' + str(self.score)
