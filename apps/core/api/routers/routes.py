from django.urls import path
from rest_framework.routers import SimpleRouter
from apps.core.api.views.plan_views import PlanListViewset

router = SimpleRouter()
router.register(r'planes', PlanListViewset, basename="planes")
urlpatterns = router.urls

