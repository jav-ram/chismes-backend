# -*- coding: utf-8 -*-
from rest_framework import viewsets
from . import models, serializers

class ChismesModelViewSet(viewsets.ModelViewSet):
    queryset = models.Chismes.objects.all()
    serializer_class = serializers.ChismesSerializer