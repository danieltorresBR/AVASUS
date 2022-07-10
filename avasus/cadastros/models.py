from django.db import models

# Create your models here.
class Modulo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    objetivo = models.CharField(max_length=200)
    idade_minima = models.IntegerField(verbose_name="Idade Mínima")

    def __str__(self):
        return "{} | {}".format(self.nome, self.descricao)

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField(verbose_name="Carga Horária")
    ordem = models.IntegerField()

    modulo = models.ForeignKey(Modulo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} | {}".format(self.nome, self.carga_horaria)



class Atividade(models.Model):
    status = models.CharField(max_length=15)
    upload = models.FileField(upload_to='uploads/')

    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return "{} | {}".format(self.status, self.curso)