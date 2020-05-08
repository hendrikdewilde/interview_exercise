from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from interview_exercise.settings import ALLOWED_HOSTS
from logs.models import StreamLogging, ApiLogging, UserLogging, BlockIP, \
    SafeIP, SmsLogging


class StreamLoggingAdmin(admin.ModelAdmin):
    model = StreamLogging
    fields = (
        'date_creation', 'level', 'traceback', 'error_time', 'file_name',
        'func_name', 'message', 'process_args', 'process_id', 'process_name',
        'ip_address',
    )
    readonly_fields = [
        'date_creation', 'level', 'traceback', 'error_time', 'file_name',
        'func_name', 'message', 'process_args', 'process_id', 'process_name',
        'ip_address',
    ]
    list_display = ('message', 'process_args', 'ip_address', 'date_creation', )
    list_filter = ('level', 'func_name', 'error_time', 'process_name', )
    search_fields = ['message', 'process_args', 'date_creation']
    actions = None

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='',
                        extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(StreamLoggingAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context)


class ApiLoggingAdmin(admin.ModelAdmin):
    model = ApiLogging
    fields = (
        'date_creation', 'user', 'status', 'method', 'path',
        'ip_address', 'host', 'cookie', 'params',
    )
    readonly_fields = [
        'date_creation', 'user', 'status', 'method', 'path',
        'ip_address', 'host', 'cookie', 'params',
    ]
    list_display = ('user', 'status', 'ip_address', 'date_creation', )
    list_filter = ('user__username', 'status', 'method',)
    search_fields = ['message', 'date_creation']
    actions = None

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='',
                        extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ApiLoggingAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context)


class UserLoggingAdmin(admin.ModelAdmin):
    model = UserLogging
    fields = (
        'date_creation', 'user', 'username', 'session_id', 'access_token',
        'ip_address', 'host', 'success',
    )
    readonly_fields = [
        'date_creation', 'user', 'username', 'session_id', 'access_token',
        'ip_address', 'host', 'success',
    ]
    list_display = ('username', 'success', 'date_creation', )
    list_filter = ('username', 'success', )
    search_fields = ['username', 'date_creation']
    actions = None

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='',
                        extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(UserLoggingAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context)


class SmsLoggingAdmin(admin.ModelAdmin):
    model = SmsLogging
    fields = (
        'date_creation', 'user', 'from_number', 'to_number', 'message',
        'sms_id',
    )
    readonly_fields = [
        'date_creation', 'user', 'from_number', 'to_number', 'message',
        'sms_id',
    ]
    list_display = ('to_number', 'sms_id', 'date_creation', )
    list_filter = ('to_number', 'sms_id', )
    search_fields = ['to_number', 'date_creation']
    actions = None

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='',
                        extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(SmsLoggingAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context)


class BlockIPAdmin(admin.ModelAdmin):
    model = BlockIP
    fields = (
        'date_creation', 'date_modified',
        'ip_address', 'reason_for_block',
    )
    readonly_fields = [
        'date_creation', 'date_modified',
    ]
    list_display = ('ip_address', 'date_creation',)
    list_filter = ('date_creation', )
    search_fields = ['ip_address']
    actions = None

    def save_model(self, request, obj, form, change):
        if form:
            if form.instance:
                if form.instance.ip_address:
                    try:
                        si_obj = SafeIP.objects.get(ip_address=form.instance.ip_address)
                    except SafeIP.DoesNotExist:
                        if form.instance.ip_address not in ALLOWED_HOSTS and \
                                str(form.instance.ip_address) != '0.0.0.0' and \
                                form.instance.ip_address is not None and \
                                form.instance.ip_address != '':
                            super().save_model(request, obj, form, change)
                    else:
                        self.message_user(request, "IP address in Save List.")


class SafeIPAdmin(admin.ModelAdmin):
    change_list_template = "logs_admin_changelist.html"

    model = SafeIP
    fields = (
        'date_creation', 'date_modified',
        'ip_address', 'reason_for_allow',
    )
    readonly_fields = [
        'date_creation', 'date_modified',
    ]
    list_display = ('ip_address', 'date_creation',)
    list_filter = ('date_creation', )
    search_fields = ['ip_address']
    actions = None

    def save_model(self, request, obj, form, change):
        if form:
            if form.instance:
                if form.instance.ip_address:
                    if form.instance.ip_address not in ALLOWED_HOSTS and \
                            str(form.instance.ip_address) != '0.0.0.0' and \
                            form.instance.ip_address is not None and \
                            form.instance.ip_address != '':
                        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('cache-flush/', self.flush),
        ]
        return my_urls + urls

    def flush(self, request):
        from django.db import connections#, transaction
        from django.core.cache import cache
        # This works as advertised on the memcached cache:
        cache.clear()
        # This manually purges the SQLite cache:
        cursor = connections['default'].cursor()
        q = """truncate table cache_table;"""
        cursor.execute(q)
        # transaction.commit_unless_managed(using='default')
        self.message_user(request, "Cache cleared.")
        return redirect('/admin/logs/safeip/')


admin.site.register(StreamLogging, StreamLoggingAdmin)
admin.site.register(ApiLogging, ApiLoggingAdmin)
admin.site.register(UserLogging, UserLoggingAdmin)
admin.site.register(SmsLogging, SmsLoggingAdmin)
admin.site.register(BlockIP, BlockIPAdmin)
admin.site.register(SafeIP, SafeIPAdmin)
