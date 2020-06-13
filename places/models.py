from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='название места')
    description_short = models.TextField(verbose_name='краткое описание')
    description_long = models.TextField(verbose_name='полное описание')
    placeId = models.CharField(max_length=255, unique=True, verbose_name='уникальный идентификатор')
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              verbose_name="место, к которому относится картинка", related_name="images")
    file = models.ImageField(upload_to='images')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="порядок отображения картинки")

    def __str__(self):
        return f"{self.order} {self.place.title}"

    class Meta(object):
        ordering = ['order']
