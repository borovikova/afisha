from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='название места')
    placeId = models.CharField(max_length=255, unique=True, verbose_name='уникальный идентификатор')
    detailsUrl = models.URLField(verbose_name='ссылка на детальные данные')
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return f"{self.title}"