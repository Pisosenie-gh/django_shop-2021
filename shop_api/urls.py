from .main.router import main_router, extra_urlpatterns

urlpatterns = []
urlpatterns += main_router.urls
urlpatterns.extend(extra_urlpatterns)
