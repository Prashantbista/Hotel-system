from django.urls import path
# from .api_views import ClientlistAPIView
from .api_views import ClientViewSet
from rest_framework.routers import DefaultRouter


router= DefaultRouter()
router.register("client", ClientViewSet, basename="client")

urlpatterns=[
    # path("client/", ClientlistAPIView.as_view(),name="client_list")
]
urlpatterns += router.urls