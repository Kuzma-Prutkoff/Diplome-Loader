from django.urls import path, include
from rest_framework import routers

from .views import CarViewSet, MaintenanceViewSet, ComplaintViewSet, UserInfoViewSet, VehicleViewSet, \
    EngineViewSet, TransmissionViewSet, DrivingAxleViewSet, SteeringAxleViewSet, MaintenanceTypeViewSet, \
    BreakageViewSet, RepairViewSet, ServiceCompanyViewSet, my_login

router = routers.DefaultRouter()
router.register('cars', CarViewSet)
router.register('maintenance', MaintenanceViewSet)
router.register('complaints', ComplaintViewSet)
router.register('users', UserInfoViewSet)
router.register('vehicles', VehicleViewSet)
router.register('engines', EngineViewSet)
router.register('transmissions', TransmissionViewSet)
router.register('driving-axles', DrivingAxleViewSet)
router.register('steering-axles', SteeringAxleViewSet)
router.register('maintenance-types', MaintenanceTypeViewSet)
router.register('breakages', BreakageViewSet)
router.register('repair-ways', RepairViewSet)
router.register('service-companies', ServiceCompanyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user-login/', my_login),
]
