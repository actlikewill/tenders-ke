from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import tender.views as views

urlpatterns = [
    path("", views.TenderListView.as_view(), name="home"),
    path("tender/<int:pk>/", views.TenderDetailView.as_view(), name="tender_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)