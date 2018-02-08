# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FilledForm(models.Model):
    job_name = models.CharField(max_length=80)
    school_name = models.CharField(max_length=80)
    gender_type = models.CharField(max_length=80)
