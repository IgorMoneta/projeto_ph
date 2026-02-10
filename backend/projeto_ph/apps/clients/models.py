from django.db import models
from django.conf import settings

class Clients(models.Model):
    id_client = models.AutoField(primary_key=True) #verificar uuid
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,        
        blank=True,
        related_name='clientes'
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11 , unique=True, null=True)
    birthday = models.DateField()
    url_photo = models.CharField(null=True)
    document = models.CharField(null=True)
    banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    