from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Diario (models.Model):
    conteudo=models.TextField(max_length=500)
    criado=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.conteudo