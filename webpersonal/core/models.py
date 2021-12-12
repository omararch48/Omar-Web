from django.db import models

# Create your models here.
class SocialNetworks(models.Model):
    title = models.CharField(max_length=200, verbose_name='Red Social')
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última modificación')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['title']
        
    def __str__(self):
        return "{}".format(self.title.title())