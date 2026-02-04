from django.db import models
import uuid





# class Banned(models.Model):

#     ACTIVE = 'ACTIVE'
#     REVOKED = 'REVOKED'
#     FINISHED = 'FINISHED'

#     STATUS_CHOICES = [
#         (ACTIVE, 'Banido'),
#         (REVOKED, 'Revogado'),
#         (FINISHED, 'Concluido')
#     ]

#     cpf = models.ForeignKey(
#         Clients,
#         on_delete=models.CASCADE, 
#         related_name='bans')
#     id_banned = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ACTIVE)
#     cause = models.CharField()
#     date_ban = models.DateTimeField()
#     expire_in = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Revocation_requests(models.Model):

#     REQUESTED = 'REQUESTED'
#     PENDING = 'PENDING'
#     APPROVED = 'APPROVED'
#     REJECTED = 'REJECTED'

#     STATUS_CHOICES = [
#         (PENDING, 'Em analise'),
#         (REQUESTED, 'Solicitação'),
#         (APPROVED, 'Aprovado'),
#         (REJECTED, 'Rejeitado')
#     ]

#     id_banned = models.ForeignKey(
#         Banned, 
#         on_delete=models.CASCADE,
#         related_name='banneds')
#     cpf = models.ForeignKey(
#         Clients, 
#         on_delete=models.CASCADE,
#         related_name='clients')
#     id_request = models.AutoField(primary_key=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=REQUESTED)
#     justification = models.CharField()
#     date_request = models.DateTimeField(auto_now_add=True)
#     date_conclusion = models.DateTimeField()
#     admin_response = models.CharField()

# class Product(models.Model):
#     TICKET = "TICKET"
#     CONSUMER = "CONSUMER"

#     PRODUCT_TYPE_CHOICES = [
#         (TICKET, 'Ticket'),
#         (CONSUMER, 'Consumer'),
#     ]

#     id = models.AutoField(primary_key=True)
#     product = models.CharField()
#     product_type = models.CharField(max_length=10, choices=PRODUCT_TYPE_CHOICES)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     active = models.BooleanField(default=True)
#     qtd = models.IntegerField()
    
# class Events(models.Model):
    
#     name = models.CharField(max_length=100),
#     describe = models.CharField(blank=True),
#     start_datetime = models.DateTimeField(),
#     end_datetime = models.DateTimeField(),
#     is_active = models.BooleanField(default=False),
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Ticket_Orders(models.Model):

#     PENDING = 'PENDING'
#     PAID = 'PAID'
#     CANCELED = 'CANCELED'
#     REFUNDED = 'REFUNDED'
#     PARTICIALLY_REFUNDED = 'PARTICIALLY_REFUNDED'

#     STATUS_CHOICES = [
#         (PENDING, 'Pendente'),
#         (PAID, 'Pago'),
#         (CANCELED, 'Cancelado'),
#         (REFUNDED, 'Reembolsado'),
#         (PARTICIALLY_REFUNDED, 'Parcialmente Reembolsado'),
#     ]

#     id = models.AutoField(primary_key=True)
#     id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING) 
#     pay_method = models.CharField(max_length=50)
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     qtd = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Ticket_Product(models.Model):
#     event_id = models.ForeignKey(
#         Events, on_delete=models.CASCADE,
#         related_name='tickets_produtos'
#     )
#     name = models.CharField(),
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     is_active = models.BooleanField(default=True)
    
# class Ticket_Order_Items(models.Model):
#     id = models.AutoField(primary_key=True)
#     ticket_product = models.ForeignKey(
#         Ticket_Product,
#         on_delete=models.CASCADE,
#         related_name='Items')
#     ticket_order_id = models.ForeignKey(
#         Ticket_Orders, 
#         on_delete=models.CASCADE,
#         related_name='Items')
#     qtd = models.PositiveIntegerField()
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

# class Ticket(models.Model):

#     VALID = 'VALID'
#     USED = 'USED'
#     CANCELED = 'CANCELED'
#     TRANSFERRED = 'TRANSFERRED'

#     STATUS_CHOICES = [
#         (VALID, 'Válido'),
#         (USED, 'Usado'),
#         (CANCELED, 'Cancelado'),
#         (TRANSFERRED, 'Transferido'),
#     ]

#     id = models.AutoField(primary_key=True) #verificar se é uuid
#     code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#     cpf = models.ForeignKey(
#         Clients, 
#         on_delete=models.CASCADE,
#         to_field='cpf'
#         )
#     id_user = models.ForeignKey(
#         Usuario, 
#         on_delete=models.CASCADE
#         )
#     ticket_order = models.ForeignKey(
#         Ticket_Order_Items, 
#         on_delete=models.CASCADE,
#         related_name='tickets')
#     event = models.ForeignKey(
#         Events, 
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True
#         )
#     used_in = models.DateTimeField()
#     validity = models.DateTimeField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=VALID)
#     token = models.CharField(unique=True, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Consumers_Orders(models.Model):

#     PENDING = 'PENDING'
#     PAID = 'PAID'
#     CANCELED = 'CANCELED'
#     REFUNDED = 'REFUNDED'
#     PARTICIALLY_REFUNDED = 'PARTICIALLY_REFUNDED'

#     STATUS_CHOICES = [
#         (PENDING, 'Pendente'),
#         (PAID, 'Pago'),
#         (CANCELED, 'Cancelado'),
#         (REFUNDED, 'Reembolsado'),
#         (PARTICIALLY_REFUNDED, 'Parcialmente Reembolsado'), 
#     ]
#     id = models.AutoField(primary_key=True)
#     id_user = models.ForeignKey(
#         Usuario, 
#         on_delete=models.CASCADE,
#         related_name='consumers_orders')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
#     pay_method = models.CharField(max_length=50)
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Consumers_Orders_Items(models.Model):
#     id = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(
#         Product, 
#         on_delete=models.CASCADE,
#         limit_choices_to={'type': Product.CONSUMER})
#     consumers_order_id = models.ForeignKey(
#         Consumers_Orders, 
#         on_delete=models.CASCADE,
#         related_name='items')
#     qtd = models.PositiveIntegerField()
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

# class Vouchers(models.Model):

#     VALID = 'VALID'
#     USED = 'USED'
#     CANCELED = 'CANCELED'
#     TRANSFERRED = 'TRANSFERRED'

#     STATUS_CHOICES = [
#         (VALID, 'Válido'),
#         (USED, 'Usado'),
#         (CANCELED, 'Cancelado'),
#         (TRANSFERRED, 'Transferido'),
#     ]

#     id = models.AutoField(primary_key=True) #verificar se é uuid
#     code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#     ticket_id = models.ForeignKey(
#         Ticket, 
#         on_delete=models.CASCADE,
#         )
#     id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     consumer_order = models.ForeignKey(
#         Consumers_Orders, 
#         on_delete=models.CASCADE,
#         related_name='consumer_orders')
#     used_in = models.DateTimeField()
#     validity = models.DateTimeField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=VALID)
#     token = models.CharField(unique=True, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)






