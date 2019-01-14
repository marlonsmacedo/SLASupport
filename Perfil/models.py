from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    
    user        = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE)
    nivel       = models.ForeignKey("Nivel", verbose_name="Nivel Interno", on_delete=models.CASCADE)
    telefone    = models.CharField(verbose_name="Contato", max_length=15)
    ramal       = models.CharField(verbose_name="Ramal", max_length=6)

class Nivel(models.Model):
    
    descricao   = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
    


