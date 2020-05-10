from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.utils.safestring import mark_safe

from claims.models import Case, Client, Document


class ClientAdmin(admin.ModelAdmin):
    model = Client
    fields = (
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
        'client_number', 'name', 'phone_number', 'address',
    )
    readonly_fields = [
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
    ]
    list_display = ('client_number', 'name', 'phone_number', 'date_creation',)
    list_filter = ('date_creation', )
    search_fields = ['client_number', 'name', 'phone_number']
    actions = None

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not obj.user_creation:
            # Only set added_by during the first save.
            obj.user_creation = request.user
        obj.user_modified = request.user
        super().save_model(request, obj, form, change)


class CaseAdmin(admin.ModelAdmin):
    model = Case
    fields = (
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
        'case_number', 'status', 'open_date', 'close_date',
        'insurance', 'insurance_consultant',
        'assessor', 'client', 'description', 'resolution',
    )
    readonly_fields = [
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
    ]
    list_display = ('case_number', 'status', 'insurance',
                    'assessor', 'client', 'date_creation',)
    list_filter = ('status', 'insurance', 'assessor', 'client',
                   'date_creation', )
    search_fields = ['case_number']
    actions = None

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not obj.user_creation:
            # Only set added_by during the first save.
            obj.user_creation = request.user
        obj.user_modified = request.user
        super().save_model(request, obj, form, change)


class DocumentAdmin(admin.ModelAdmin):
    model = Document
    fields = (
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
        'document_type', 'name', 'file_name', 'case',
    )
    readonly_fields = [
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
    ]
    list_display = ('document_type', 'name', 'case', 'file_open_new_tab', 'date_creation',)
    list_filter = ('document_type', 'date_creation', )
    search_fields = ['name', 'case']
    actions = None

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not obj.user_creation:
            # Only set added_by during the first save.
            obj.user_creation = request.user
        obj.user_modified = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['file_name']
        return self.readonly_fields

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.fields = (
                'date_creation', 'date_modified',
                'user_creation', 'user_modified',
                'document_type', 'name', 'case',
            )
        else:
            self.fields = (
                'date_creation', 'date_modified',
                'user_creation', 'user_modified',
                'document_type', 'name', 'file_name', 'case',
            )

        form = super(DocumentAdmin, self).get_form(request, obj, **kwargs)
        return form

    @staticmethod
    def file_open_new_tab(obj):
        if obj.file_name:
            filename_long = str(obj.file_name)
            filename = filename_long.rsplit('/', 1)[1]
            return mark_safe('<a href="/media/{}"  target="_blank">{}</a>'.
                             format(filename_long, filename))
        else:
            return


admin.site.register(Client, ClientAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Document, DocumentAdmin)
