from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Nota

class NotaAdmin(admin.ModelAdmin):
	list_display = ['nome', 'primeira_nota', 'segunda_nota', 'terceira_nota', 'quarta_nota','media_notas', 'status_do_aluno']

	def status_do_aluno(self, obj):
		if 7 > obj.media_notas >=5:
			return "RECUPERAÇÃO"
		elif obj.media_notas < 5:
			return "REPROVADO"
		#else:
		elif obj.media_notas >= 7:
			return "APROVADO"
		return format_html(obj.media_notas)


admin.site.register(Nota, NotaAdmin)
