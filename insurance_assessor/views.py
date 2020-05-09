import logging

from django.shortcuts import render

log = logging.getLogger(__name__)


def insurance_assessor_index(request):
    return render(request, 'insurance_assessor_index.html',
                  {})
