from django.urls import path

from .views import HousingViewSet, NeighborhoodViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('neighborhood', NeighborhoodViewSet, basename='neighborhood')
router.register('', HousingViewSet, basename='housing')

urlpatterns = router.urls

#**** Below is the first version (per the tutorial)

# from .views import ListHousing, DetailHousing

# urlpatterns = [
#     path('', ListHousing.as_view()),
#     path('<int:pk>/', DetailHousing.as_view()),
# ]