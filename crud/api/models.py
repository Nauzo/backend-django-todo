from django.db import models
#para mostrar el listado en panel django
class Tarea(models.Model):
    body = models.CharField(max_length=50)

    def __str__(self):
        return  self.body