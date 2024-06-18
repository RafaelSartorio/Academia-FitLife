from django.contrib import admin
from core.models import Aulas


class AulaAdmin(admin.ModelAdmin):
    list_display = ('nomeAula' , 'data_aula')

admin.site.register(Aulas , AulaAdmin)
#
