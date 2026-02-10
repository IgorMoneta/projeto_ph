from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path("cadastrar/", CreateUserView.as_view(), name="cadastrar")
]