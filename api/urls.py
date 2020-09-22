from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'bank_info',views.BankViewSet)

urlpatterns = [
    path('auth/',include('rest_framework.urls')),
    path('',include(router.urls)),
]