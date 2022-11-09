from django.db import models

# Create your models here.

class Nombre(models.Model):
    # Un campo para poder escribir
    body = models.TextField()
    # Se usa para saber cada vez que se modifica el campo de texto
    updated =  models.DateTimeField(auto_now=True)
    # Se crea una marca cada vez que se crea algo dentro del campo 
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.body[0:50]
    
    class Meta:
        # Atributo que permite que la lista de lo creado se ubique en el tope
        ordering = ['-updated']