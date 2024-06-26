from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  CarBookingViewSet,  CarViewSet

# Create a router and register the viewsets with basename
router = DefaultRouter()
# router.register(r'carimage', CarImageViewSet, basename='carimage')
# router.register(r'carmake', CarMakeViewSet, basename='carmake')
# router.register(r'carmodel', CarModelViewSet, basename='carmodel')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'bookings', CarBookingViewSet, basename='carbooking')

urlpatterns = [
    # Your other URL patterns go here if you have any
    path('api/', include(router.urls)),
]
