import uuid
from django.db import models


class BaseModel(models.Model):
    """
    Base model for other models
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at datetime'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated at datetime'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is active?'
    )

    class Meta:
        abstract = True

    @classmethod
    def get_all_default_model_fields_name(cls):
        """
        Return list of all fields of this model
        """
        field_name = []
        for field in cls._meta.fields:
            field_name.append(field.name)
        return field_name

    @classmethod
    def active(cls):
        """
        Get list of active objects
        @return: Filtered queryset
        """
        return cls.objects.filter(is_active=True)

    @classmethod
    def inactive(cls):
        """
        Get list of inactive objects
        @return: Filtered queryset
        """
        return cls.objects.filter(is_active=False)

