from rest_framework import routers
from .api import MeasurementUser,LogViewSet,LogMeasureSet,PatientViewSet,MeasurementViewSet,RiskViewSet,GetSpecificMeasureViewSet,GetSpecificRiskViewSet

router = routers.DefaultRouter()
router.register('api/patient',PatientViewSet,'patient')
router.register('api/risk',RiskViewSet,'risk')
router.register('api/measurement',MeasurementViewSet,'measurement')
router.register('api/measurement/<pk>/',MeasurementViewSet,'measurement')
router.register('api/specmeasure',GetSpecificMeasureViewSet,'specmeasure')
router.register('api/specrisk',GetSpecificRiskViewSet,'specrisk')
router.register('api/log',LogViewSet,'log')
router.register('api/loglog',LogMeasureSet,'loglog')
router.register('api/measureuser',MeasurementUser,'measureuser')
urlpatterns = router.urls