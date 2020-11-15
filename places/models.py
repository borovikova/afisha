from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='название места')
    short_description = models.TextField(verbose_name='краткое описание', blank=True)
    long_description = HTMLField(verbose_name='полное описание', blank=True)
    place_id = models.CharField(max_length=255, unique=True, verbose_name='уникальный идентификатор')
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return f"{self.title}"

    class Meta(object):
        verbose_name = "локация"
        verbose_name_plural = "локации"


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              verbose_name="место, к которому относится картинка", related_name="images")
    file = models.ImageField(upload_to='images')
    order = models.PositiveIntegerField(default=0, verbose_name="порядок отображения картинки")

    def __str__(self):
        return f"{self.order} {self.place.title}"

    class Meta(object):
        ordering = ['order']
