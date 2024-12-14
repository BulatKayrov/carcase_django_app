from django.db import models

from core.mixins.model.time_at import TimeAtMixin


class YouModel(TimeAtMixin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'you_model_name'
        verbose_name_plural = 'you_model_name'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        pass
