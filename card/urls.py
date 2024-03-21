from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ex: /card/
    path("", views.index, name="index"),
    # ex: /card/3/
    path("<int:card_id>/", views.detail, name="detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)