from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("predict_post", views.predict_data.as_view(), name="predict_post"),
]
