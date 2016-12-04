# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def podii(request):
        podii = (
          {'name': u'подія 1',
          'text': u'sdfsfvsd'},
          {'name': u'подія 2',
          'text': u'second'}
        )
	return render(request, 'students/podii.html', 
		{'podii': podii})
###

def biblioteka(request):
	return render(request, 'students/biblioteka.html', {})

###
def vyhovna(request):
	return render(request, 'students/vyhovna.html', {})

###
def muzey(request):
	return render(request, 'students/muzey.html', {})

###
def kolek(request):
	return render(request, 'students/kolek.html', {})

###
def psuholoh(request):
	return render(request, 'students/psuholoh.html', {})

###
def zno(request):
	return render(request, 'students/zno.html', {})

###
def rozlad(request):
	return render(request, 'students/rozlad.html', {})

###
def istoria(request):
	return render(request, 'students/istoria.html', {})


