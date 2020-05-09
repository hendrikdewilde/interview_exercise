import logging

from django.shortcuts import render

log = logging.getLogger(__name__)


def cases_index(request):
    return render(request, 'cases_index.html',
                  {})
