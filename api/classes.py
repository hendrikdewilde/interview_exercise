from rest_framework import permissions
from rest_framework.metadata import BaseMetadata


class IsAuthenticatedAndReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return super(IsAuthenticatedAndReadOnly, self).has_permission(
                request, view)


class APIRootMetadata(BaseMetadata):
    """
    Don't include field and other information for `OPTIONS` requests.
    Just return the name and description.
    """
    def determine_metadata(self, request, view):

        if view.get_view_name() == "Networks List":
            actions = {
                "GET": {
                    "read_only": True,
                    "parameters required": False,
                    "parameters": {},
                },
            }
        elif view.get_view_name() == "Connection List":
            actions = {
                "GET": {
                    "read_only": True,
                    "parameters required": True,
                    "parameters": {
                        "network_code": "enter 'network code' to filter by, "
                                        "if empty will skip. (example: LINE)",
                        "invoice_date": "enter 'invoice date' to filter by, "
                                        "(example: 2019-07-30)",
                    },
                },
            }
        else:
            actions = {}
        return {
            'name': view.get_view_name(),
            'description': view.get_view_description(),
            'renders': [renderer.media_type for renderer in
                        view.renderer_classes],
            'parses': [parser.media_type for parser in view.parser_classes],
            'actions': actions,
        }
