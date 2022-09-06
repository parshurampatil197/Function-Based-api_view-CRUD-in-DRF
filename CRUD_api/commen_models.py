from django.db import models
# from django_userforeignkey.models.fields import UserForeignKey
# from ..managers.default_manager import DefaultManager


class CommonFields(models.Model):
    # Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True,
    #                            blank=True)
    # updated_by = UserForeignKey(auto_user=True, auto_user_add=True, related_name='updated_%(class)s_set')

    # Managers
    # objects = DefaultManager()

    # Meta
    class Meta:
        abstract = True
