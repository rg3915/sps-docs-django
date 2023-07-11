from django.db import models


class SPSElement(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'SPSElement'
        verbose_name_plural = 'SPSElements'

    def __str__(self):
        return f'{self.name}'
