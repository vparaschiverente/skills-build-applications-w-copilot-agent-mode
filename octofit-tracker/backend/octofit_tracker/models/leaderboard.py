from djongo import models

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    team = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.user} - {self.score}"
