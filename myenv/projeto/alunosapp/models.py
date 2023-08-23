from django.db import models
from datetime import date #importa o calendário widget
from simple_history.models import HistoricalRecords #para armazenar os dados históricamente
from django.contrib.auth.models import User #A classe User faz parte do sistema de autenticação do Django
from django.core.validators import MinValueValidator #para validações
from decimal import Decimal #para adicionar decimais (está sendo usado na variável peso)

# Create your models here.

# o nome da class é referente ao título da tabela

#tabela Alunos
class Alunos(models.Model):
    verbose_name = "Alunos"
    
    #opções para gênero
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    #opções para objetivo de frequência
    DIAS_DA_SEMANA_CHOICES = (
        (1, '1 dia por semana'),
        (2, '2 dias por semana'),
        (3, '3 dias por semana'),
        (4, '4 dias por semana'),
        (5, '5 dias por semana'),
        (6, '6 dias por semana'),
        (7, 'Todos os dias'),
    )

    #opções para objetivo de treino
    EMAGRECIMENTO = 'Emagrecimento'
    HIPERTROFIA = 'Hipertrofia'
    REABILITACAO = 'Reabilitação'
    SAUDE = 'Saúde'

    OBJETIVO_CHOICES = (
        (EMAGRECIMENTO, 'Emagrecimento'),
        (HIPERTROFIA, 'Hipertrofia'),
        (REABILITACAO, 'Reabilitação'),
        (SAUDE, 'Saúde'),
    )

    nome = models.CharField(max_length=100) 
    data_de_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        help_text='Formato: dd/mm/aaaa',
    )
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    idade = models.IntegerField()
    
    altura_em_cm = models.PositiveIntegerField()
    peso_em_kg = models.DecimalField(
        max_digits=5,  # Ajuste o número de dígitos conforme necessário
        decimal_places=2,  # Duas casas decimais
        validators=[MinValueValidator(Decimal('0.01'))]
    )

    dias_semana_objetivo = models.IntegerField(
        choices=DIAS_DA_SEMANA_CHOICES,
    )
    objetivo = models.CharField(max_length=20, choices=OBJETIVO_CHOICES, null=True)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    usa_aplicativo = models.BooleanField(default=False)
    
    #função para calcular a idade de cada pessoa automaticamente com o input da classe data de nascimento
    def idade(self):
        today = date.today()
        delta = today - self.data_de_nascimento
        years = delta.days // 365
        return years
    
    historical = HistoricalRecords() #para gravar as alterações

    #define como os registros vão aparecer no admin, no caso, será pelo nome
    def __str__(self):
        return self.nome