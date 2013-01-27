from django.db import models

class Game(models.Model):
    password = models.CharField(max_length = 100)
    round = models.IntegerField(default = 0)
    round_1_master_bpm = models.PositiveIntegerField(null = True)
    round_2_master_bpm = models.PositiveIntegerField(null = True)
    round_3_master_bpm = models.PositiveIntegerField(null = True)
    host = models.ForeignKey("Player", related_name = "hosted")
    max_bpm = models.PositiveIntegerField(default = 0)
    max_bpm_player = models.ForeignKey("Player", null = True, related_name = "max_player")
    min_bpm = models.PositiveIntegerField(default = 50000)
    min_bpm_player = models.ForeignKey("Player", null = True, related_name = "min_player")

class Player(models.Model):
    name = models.CharField(max_length = 100)
    game = models.ForeignKey(Game, null = True, related_name = "players")
    round_1_bpm = models.PositiveIntegerField(null = True)
    round_2_bpm = models.PositiveIntegerField(null = True)
    round_3_bpm = models.PositiveIntegerField(null = True)
    score = models.IntegerField(default = 0)
    score_summary = models.TextField()
    class Meta:
        unique_together = ("name", "game")
