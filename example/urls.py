from django.urls import path

from .views import ExampleFormView

urlpatterns = [
    path('', ExampleFormView.as_view()),
]
