# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render
from scripts import convert
from scripts import extract_from_txt
from scripts import calcul_stat

def home(request):
    context = {
        'job_titles': ['Ingenieur', 'test', 'chomeur', 'all'],
        'schools': ['ECE', 'all'],
        'genders': ['Female', 'Male', 'all'],
    }
    return render(request, 'main/index.html', context)


def job(request, job_title='all', school='all', gender='all'):
    context = {
        'job_title': job_title,
        'school': school,
        'gender': gender,
    }
    return render(request, 'main/results.html', context)
