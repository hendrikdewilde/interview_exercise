import datetime
import logging

from rest_framework import viewsets

from api.classes import IsAuthenticatedAndReadOnly, APIRootMetadata
# from api.serializers import NetworkSerializer, ConnectionSerializer
from logs.models import ApiLogging

log = logging.getLogger(__name__)


