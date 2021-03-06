from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'person', views.PersonViewSet)
router.register(r'book', views.BookView, basename='book')
# router.register(r'book/associates/', views.AssociatedPerson)



urlpatterns = [
    path('', include(router.urls)),
    path('person/', include('rest_framework.urls', namespace='rest_framework'))
]