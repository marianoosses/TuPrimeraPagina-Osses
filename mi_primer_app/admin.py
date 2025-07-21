from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso,Profesor

register_models = [Familiar, Curso,Profesor]

admin.site.register(register_models)
