from rest_framework import viewsets
from apps.core.models import Plan
from apps.core.api.serializers.plan_serializers import PlanSerializer

class PlanListViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer