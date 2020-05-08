import logging

from rest_framework import serializers

log = logging.getLogger(__name__)


# class NetworkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Network
#         fields = ['code', 'price_category_code', 'get_connection_list',
#                   'get_gateway_connection_list']
#
#
# class ConnectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Connection
#         fields = ['connection_id', 'active', 'solar']
