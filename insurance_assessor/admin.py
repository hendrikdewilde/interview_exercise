from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from insurance_assessor.models import Assessor


class AssessorAdmin(admin.ModelAdmin):
    model = Assessor
    fields = (
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
        'name', 'phone_number', 'linked_user',
    )
    readonly_fields = [
        'date_creation', 'date_modified',
        'user_creation', 'user_modified',
    ]
    list_display = ('name', 'phone_number', 'linked_user', 'date_creation',)
    list_filter = ('linked_user', 'date_creation', )
    search_fields = ['name', 'linked_user']
    actions = None

    def render_change_form(self, request, context, *args, **kwargs):
        from django.contrib.auth.models import User

        context['adminform'].form.fields[
            'linked_user'].queryset = User.objects.\
            prefetch_related('groups').\
            filter(groups__name='Assessors')
        return super(AssessorAdmin, self).render_change_form(
            request, context, *args, **kwargs)

    # This will help you to disable delete functionality
    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if not obj.user_creation:
            # Only set added_by during the first save.
            obj.user_creation = request.user
        obj.user_modified = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Assessor, AssessorAdmin)
