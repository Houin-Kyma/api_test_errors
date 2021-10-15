from django.urls import path

from .views import OprosView

app_name = "oprosnik"

urlpatterns = [
    path('oprosnik/', OprosView.as_view()),
]