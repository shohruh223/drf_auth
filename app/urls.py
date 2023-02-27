from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import ProductView, UserView, GetMeView

router = DefaultRouter()
router.register('product', ProductView)
# router.register('user', UserView)


urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserView.as_view()),
    path('getme/', GetMeView.as_view())
]