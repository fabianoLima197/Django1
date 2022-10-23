from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=1000)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'