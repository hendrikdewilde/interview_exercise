import logging

from django.shortcuts import render

log = logging.getLogger(__name__)


def logs_index(request):
    return render(request, 'logs_index.html',
                  {})
