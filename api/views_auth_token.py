import logging

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

from gen_lib.utils import get_user_obj_by_name_db, get_client_ip
from logs.models import UserLogging

log = logging.getLogger(__name__)


class ObtainAuthTokenCustom(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser,
                      parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    @classmethod
    def get_extra_actions(cls):
        return []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=False)
        if serializer.validated_data:
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            user_obj = get_user_obj_by_name_db(user)

            login_obj = UserLogging()
            login_obj.username = user or None
            login_obj.user = user_obj or None
            login_obj.access_token = token.key
            login_obj.ip_address = get_client_ip(request) or None
            login_obj.host = request.META.get('HTTP_HOST') or None
            login_obj.success = True
            login_obj.save()

            return Response({'token': token.key})
        else:
            return Response({'message': "invalid login"})


obtain_auth_token_custom = ObtainAuthTokenCustom.as_view()
