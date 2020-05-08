import logging

from django.shortcuts import render

from logs.models import StreamLogging

log = logging.getLogger(__name__)


def logs_index(request):
    return render(request, 'logs_index.html',
                  {})
