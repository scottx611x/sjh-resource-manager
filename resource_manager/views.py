from django.http import HttpResponseServerError
from rest_framework import viewsets

from resource_manager.models import JupyterUser
from resource_manager.serializers import JupyterUserSerializer


class JupyterUserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = JupyterUser.objects.all()
    serializer_class = JupyterUserSerializer
    lookup_value_regex = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'
    lookup_field = "email"
    http_method_names = ["get", "put"]

    def get_object(self):
        if self.request.method == 'PUT':
            try:
                JupyterUser.objects.get(
                    email=self.kwargs.get('email')
                )
            except JupyterUser.MultipleObjectsReturned:
                return HttpResponseServerError()
            except JupyterUser.DoesNotExist:
                return JupyterUser.objects.create(
                    email=self.kwargs.get('email')
                )
            else:
                return JupyterUser.objects.get(
                    email=self.kwargs.get('email')
                )

        else:
            return super(JupyterUserViewSet, self).get_object()
