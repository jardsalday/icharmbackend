from rest_framework import routers
from .api import MedicViewSpecific,UserForAdmin,MedicUserViewSet,GetPatientViewSet,PatientUserViewSet,GetMedicsViewSet,PatientViewSpecific
from .api import GetAdminPatientViewSet,GetAdminMedicViewSet,MedicForUser,SearchPatientViewSet,SearchAdminPatientViewSet
router = routers.DefaultRouter()
router.register('api/users',UserForAdmin,'users')
router.register('api/users/<pk>',UserForAdmin,'updateusers')
router.register('api/registermedic',MedicUserViewSet,'registermedic')
router.register('api/registerpatient',PatientUserViewSet,'registerpatient')
router.register('api/getpatient',GetPatientViewSet,'getpatient')
router.register('api/getmedic',GetMedicsViewSet,'getmedic')
router.register('api/getspecific',PatientViewSpecific,'getspecific')
router.register('api/getmedicspecific',MedicViewSpecific,'getmedicspecific')
router.register('api/getallpatient',GetAdminPatientViewSet,'getallpatient')
router.register('api/getallmedic',GetAdminMedicViewSet,'getallmedic')
router.register('api/medicforuser',MedicForUser,'medicforuser')
router.register('api/searchweb',SearchPatientViewSet,'searchweb')
router.register('api/searchpatadmin',SearchAdminPatientViewSet,'searchpatadmin')
urlpatterns = router.urls