import logging

from django.shortcuts import render

log = logging.getLogger(__name__)


def claims_index(request):
    return render(request, 'claims_index.html',
                  {})
