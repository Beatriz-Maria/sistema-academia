from django.contrib import admin
from .models import Alunos

# Register your models here.

admin.site.register(Alunos)
admin.site.register(Alunos.historical.model)
