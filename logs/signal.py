import logging

from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver

from gen_lib.functions import get_client_ip, get_client_session_id, \
    get_user_obj_by_name_db
from logs.models import UserLogging

log = logging.getLogger(__name__)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    user_obj = get_user_obj_by_name_db(user)

    # Add to login log
    login_obj = UserLogging()
    login_obj.username = user or None
    login_obj.user = user_obj or None
    login_obj.session_id = get_client_session_id(request) or None
    login_obj.ip_address = get_client_ip(request) or None
    login_obj.host = request.META.get('HTTP_HOST') or None
    login_obj.success = True
    login_obj.save()


@receiver(user_login_failed)
def user_login_failed_callback(credentials, request, **kwargs):
    username = credentials['username'] # get the username.
    user_obj = get_user_obj_by_name_db(username)

    # Add to login log
    login_obj = UserLogging()
    login_obj.username = username or None
    login_obj.user = user_obj or None
    # login_obj.session_id = get_client_session_id(request) or None
    login_obj.ip_address = get_client_ip(request) or None
    login_obj.host = request.META.get('HTTP_HOST') or None
    login_obj.success = False
    login_obj.save()
