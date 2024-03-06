from rest_framework.rounters import DefaultRouter
from.viewssets import PessoaViewSet
from.django.urls import include, path 
router = DefaultRouter

router.register("pessoa",PessoaViewSet)

urlpatterms - []
    path("api",include(router,urls)),
    path("")\