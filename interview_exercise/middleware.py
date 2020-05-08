from django import http
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

from logs.models import BlockIP


class BlockedIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        is_banned = False

        # Disable this function for now
        try:
            ip = request.META['REMOTE_ADDR']
        except:
            pass
        else:
            block_ips = cache.get('blockip:list')
            if block_ips is None:
                block_ips = BlockIP.objects.all()
                cache.set('blockip:list', block_ips)
            deny_ips = [i.ip_address for i in block_ips]

            for ip_address in deny_ips:
                if ip == ip_address:
                    is_banned = True
                    break

            if is_banned:
                # delete sessions when denied
                for k in request.session.keys():
                    del request.session[k]
                return http.HttpResponseForbidden('<h1>Forbidden</h1>')
