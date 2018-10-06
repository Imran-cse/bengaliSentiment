from django.db import models

class WordList(models.Model):
    word = models.CharField(max_length=20)
    avg_polarity = models.FloatField(null=True)

class Polarity(models.Model):
    word_id = models.ForeignKey(WordList, on_delete=models.CASCADE)
    valence = models.FloatField()
