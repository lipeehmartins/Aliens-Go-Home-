from django.urls import path, include
from .views import HistoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('history', HistoryViewSet, basename='history')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]