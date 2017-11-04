# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.core import serializers
from django.shortcuts import render
from practice_d3.app.models import Hotentry


def d3(request):
    data = serializers.serialize('json', Hotentry.objects.all())
    return render(request, 'd3.html', {'context': data})
