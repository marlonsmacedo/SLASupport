from django.contrib.auth.models import User
from django.db import models


class Area(models.Model):

    desc_area = models.CharField(max_length=50, verbose_name="Área de Atendimento")

    def __str__(self):
        return self.desc_area


class Problema(models.Model):

    desc_problema = models.CharField(max_length=50, verbose_name="Problema")
    area = models.ForeignKey("Area", verbose_name="Área", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Problema"
        verbose_name_plural = "Problemas"

    def __str__(self):
        return self.desc_problema


class Categoria_Problema(models.Model):

    problema = models.ForeignKey("Problema", verbose_name="Problema", on_delete=models.CASCADE)
    desc_categoria_problema = models.CharField(max_length=50, verbose_name="Categoria Problema")
    sla = models.PositiveSmallIntegerField(default=24)
    tipo_manutencao = models.CharField(verbose_name="Tipo Manutenção", max_length=50, default="suporte")

    def __str__(self):
        return self.desc_categoria_problema


class Status_Chamado(models.Model):

    status = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Status_Chamado"
        verbose_name_plural = "Status_Chamados"

    def __str__(self):
        return self.status


class Chamado(models.Model):

    LOCAL_CHOICES = (
        ('LOCAL', 'LOCAL'),
        ('Àrea de Vendas', 'Àrea de Vendas'),
        ('CPD', 'CPD'),
        ('Tesouraria', 'Tesouraria'),
        ('Gerência', 'Gerência'),
        ('Departamento Pessoal', 'Departamento Pessoal'),
        ('Deposito', 'Deposito'),
        ('Açougue', 'Açougue'),
        ('Padaria', 'Padaria'),
        ('Salgados', 'Salgados'),
        ('Açougue', 'Açougue'),
        ('Hortifruti', 'Hortifruti'),
        ('Laticínios', 'Laticínios'),
    )

    UNIDADES_CHOICES = (
        ('Unidade', 'Unidade'),
        ('Filial 01', 'Filial 01'),
        ('Filial 02', 'Filial 02'),
        ('Filial 03', 'Filial 03'),
        ('Filial 04', 'Filial 04'),
        ('Filial 05', 'Filial 05'),
        ('Filial 06', 'Filial 06'),
        ('Filial 07', 'Filial 07'),
        ('Filial 08', 'Filial 08'),
        ('Filial 09', 'Filial 09'),
        ('Filial 10', 'Filial 10'),
        ('Filial 11', 'Filial 11'),
        ('Filial 12', 'Filial 12'),
        ('Filial 13', 'Filial 13'),
        ('Filial 15', 'Filial 15'),
        ('Filial 16', 'Filial 16'),
        ('Carga Seca', 'Carga Seca'),
        ('Carga Fria', 'Carga Fria'),
        ('Città América', 'Città América'),
        ('Downtown', 'Downtown'),
    )

    area = models.ForeignKey("Area", verbose_name="Área", on_delete=models.CASCADE)
    problema = models.ForeignKey("Problema", verbose_name="Problema", on_delete=models.CASCADE)
    categoria_problema = models.ForeignKey("Categoria_Problema", verbose_name="Categoria_problema", on_delete=models.CASCADE)
    criador = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.CASCADE)
    ramal = models.CharField(max_length=15, default="4392")
    unidade = models.CharField(verbose_name="Unidade", max_length=100, choices=UNIDADES_CHOICES, default="UNIDADE")
    local = models.CharField(verbose_name="Local", max_length=100, choices=LOCAL_CHOICES, default="LOCAL")
    dt_abertura = models.DateTimeField(auto_now_add=True)
    dt_alterado = models.DateTimeField(auto_now=False, blank=True, null=True)
    dt_fechamento = models.DateTimeField(auto_now=False, blank=True, null=True)
    desc_problema = models.TextField(verbose_name="Descricão Problema", blank=True, default="Por favor descreva o Problema Ocorrido.")
    desc_solucao = models.TextField(verbose_name="Descricão Solução", blank=True, default="Por favor descreva a Solução do Problema.")
    desc_sla_justificativa = models.TextField(verbose_name="Descricão Estouro SLA", blank=True, default="Por favor descreva a Justificativa para o estouro do SLA.")
    status_chamado = models.ForeignKey("status_chamado", verbose_name="Status", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"

    def __str__(self):
        return str(self.id)
