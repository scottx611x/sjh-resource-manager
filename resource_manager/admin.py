from django.contrib import admin
from .models import JupyterUser, JupyterNode


class AdminFieldPopulator(admin.ModelAdmin):
    """
    Wrapper around ModelAdmin that exposes all of a Model's fields in admin ui
    """
    def __init__(self, model, admin_site):
        super(AdminFieldPopulator, self).__init__(model, admin_site)
        self.list_display = [field.name for field in model._meta.fields]


class JupyterUserAdmin(AdminFieldPopulator):
    pass


class JupyterNodeAdmin(AdminFieldPopulator):
    pass

admin.site.register(JupyterUser, JupyterUserAdmin)
admin.site.register(JupyterNode, JupyterNodeAdmin)