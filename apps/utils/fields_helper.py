from django.db.models.fields.files import ImageFieldFile
from rest_framework.serializers import Field


class PathSerializerField(Field):
    def __init__(self, path=None, **kwargs):
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        self.path = path
        super(PathSerializerField, self).__init__(**kwargs)
    
    def to_internal_value(self, data):
        pass
    
    def to_representation(self, value):
        field_name = self.field_name
        if self.path:
            attrs = self.path.split('.')
            for attr in attrs:
                if hasattr(value, attr):
                    value = getattr(value, attr)
            if isinstance(value, ImageFieldFile):
                if value.name == '':
                    return None
                else:
                    return self.context['request'].build_absolute_uri(value.url)
            return value
        return getattr(value, field_name)
