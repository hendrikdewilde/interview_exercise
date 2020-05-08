import logging

from django.db import DatabaseError


class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        from django.core.cache import cache
        from logs.models import StreamLogging
        from interview_exercise.settings import ALLOWED_HOSTS
        from logs.models import BlockIP, SafeIP

        record.ip = '0.0.0.0'
        try:
            request = record.request
            record.ip = request.META.get('REMOTE_ADDR')
        except:
            try:
                request = record.args[0]
                record.ip = request.META.get('REMOTE_ADDR')
            except:
                pass

        try:
            sl_obj = StreamLogging.objects.create(
                level=record.levelname,
                traceback=record.exc_info,
                error_time=record.created,  # Format as datetime
                file_name=record.filename,
                func_name=record.funcName,
                message=record.msg,
                process_id=record.process,
                process_name=record.processName,
                process_args=record.args,
                ip_address=record.ip
            )
        except DatabaseError:
            pass
        else:
            if sl_obj:
                if sl_obj.level == 'WARNING':
                    if sl_obj.ip_address not in ALLOWED_HOSTS and \
                            str(sl_obj.ip_address) != '0.0.0.0' and \
                            sl_obj.ip_address is not None and \
                            sl_obj.ip_address != '':
                        try:
                            si_obj = SafeIP.objects.get(
                                ip_address=sl_obj.ip_address)
                        except SafeIP.DoesNotExist:
                            if sl_obj.process_args is not None:
                                if 'Not Found' in sl_obj.process_args or \
                                        'Forbidden' in sl_obj.process_args or \
                                        'CSRF cookie not set.' in sl_obj.process_args or \
                                        'Bad Request' in sl_obj.process_args:
                                    try:
                                        BlockIP.objects.create(
                                            ip_address=sl_obj.ip_address,
                                            reason_for_block="Auto added by system."
                                        )
                                    except DatabaseError:
                                        pass
                                    else:
                                        block_ips = BlockIP.objects.all()
                                        cache.set('blockip:list', block_ips)
