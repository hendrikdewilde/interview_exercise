import logging

from django.shortcuts import render

log = logging.getLogger(__name__)


def insurance_companies_index(request):
    return render(request, 'insurance_companies_index.html',
                  {})
