# -*- Mode: Python; coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class Nota(models.Model):
	nome = models.CharField(u'Nome do Aluno', max_length=150)
	primeira_nota = models.IntegerField(u'1º Bimestre')
	segunda_nota = models.IntegerField(u'2º Bimestre')
	terceira_nota = models.IntegerField(u'3º Bimestre')
	quarta_nota  = models.IntegerField(u'4º Bimestre')
	media_notas = models.IntegerField(u'Média', blank=True, default=0)

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		self.media_notas = (self.primeira_nota + self.segunda_nota + self.terceira_nota + self.quarta_nota) / 4
		return super(Nota, self).save(*args, **kwargs)