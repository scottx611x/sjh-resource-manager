from django.contrib import admin
from .models import CustomUser, Node


class AdminFieldPopulator(admin.ModelAdmin):
    """
    Wrapper around ModelAdmin that exposes all of a Model's fields in admin ui
    """
    def __init__(self, model, admin_site):
        super(AdminFieldPopulator, self).__init__(model, admin_site)
        self.list_display = [field.name for field in model._meta.fields]


class CustomUserAdmin(AdminFieldPopulator):
    pass


class NodeAdmin(AdminFieldPopulator):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Node, NodeAdmin)