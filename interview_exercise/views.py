import logging

from django.shortcuts import render, redirect

from gen_lib.utils import get_client_session_id

log = logging.getLogger(__name__)


def index(request):
    session_id = get_client_session_id(request)
    return render(request, 'index.html', {})
