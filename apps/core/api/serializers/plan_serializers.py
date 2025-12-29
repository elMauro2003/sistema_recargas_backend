from rest_framework import serializers
from apps.core.models import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'titulo', 'descripcion', 'precio', 'beneficios', 'es_popular']