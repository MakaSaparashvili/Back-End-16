from rest_framework import serializers
from .models import Article

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ArticleSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
