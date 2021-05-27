from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'postmessage', views.PostMessageViewSet)
router.register(r'interaction', views.InteractionViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('posts/', views.myapp_post, name='myapp'),
]
