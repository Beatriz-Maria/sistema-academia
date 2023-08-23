from django.shortcuts import render
from django.http import JsonResponse #para criar os graficos com CHartsJS
from alunosapp.models import Alunos


# Create your views here.
def home(request):
    return render(request, 'alunosapp/home.html')

#função view - gráfico de genero
def gender_chart_data(request):
    # Consulta o banco de dados para obter a contagem de alunos por gênero
    male_count = Alunos.objects.filter(genero='M').count() #Consultando o banco de dados para obter a contagem de alunos por gênero usando o método filter com base no campo genero da sua mode
    female_count = Alunos.objects.filter(genero='F').count() 
    other_count = Alunos.objects.filter(genero='O').count()

    # Criando um dicionário data com duas listas, uma para os rótulos (labels) e outra para os dados (data) que serão usados para criar o gráfico.
    data = {
        'labels': ['Masculino', 'Feminino', 'Outro'],
        'data': [male_count, female_count, other_count],
    }

    # Retorne os dados como uma resposta JSON
    return JsonResponse(data)
