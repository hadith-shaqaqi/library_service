from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'author', views.AuthorViewSet)
router.register(r'publisher', views.PublisherViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'book_details', views.BookDetailsViewSet, basename='bookdetails')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
