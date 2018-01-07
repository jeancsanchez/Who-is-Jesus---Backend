from rest_framework import routers

from verses.views import VerseViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'verses', VerseViewSet, base_name='verse')
urlpatterns = router.urls
