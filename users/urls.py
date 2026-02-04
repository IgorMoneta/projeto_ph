from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("cadastrar/", RegisterView.as_view(), name="cadastrar")
]