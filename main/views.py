# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, Http404, StreamingHttpResponse
from django.shortcuts import render, redirect

from .forms import RequestForm
from scripts.convert import listExperienceTitle
from scripts import extract_from_txt


def home(request):
    context = {
        'job_titles': listExperienceTitle,
        'schools': ['ECE', 'all'],
        'genders': ['Female', 'Male', 'all'],
    }
    return render(request, 'main/index.html', context)


def index(request):
    job = ''
    school = ''
    gender = ''

    form = RequestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            context = {
                'job_title': form.cleaned_data['job'],
                'school': form.cleaned_data['school'],
                'gender': form.cleaned_data['gender'],
            }

            return render(request, 'main/results.html', context)

    context = {'form': form, 'job': job, 'school': school, 'gender': gender}

    return render(request, 'main/index.html', context)


def job(request, job_title='all', school='all', gender='all'):
    context = {
        'job_title': request.POST['job'],
        'school': school,
        'gender': gender,
    }
    return render(request, 'main/results.html', context)

# Getters
