from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        fields_param = self.request.query_params.get('fields')
        if fields_param:
            fields = fields_param.split(',')
            kwargs['fields'] = fields
        return serializer_class(*args, **kwargs)

