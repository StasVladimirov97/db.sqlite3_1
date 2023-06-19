from typing import Sequence
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Order, Product


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Create order with product")
        user = User.objects.get(username="admin")
        products: Sequence[Product] = Product.objects.all()
        order, created = Order.objects.get_or_create(
            delivery_address="ul Ivanova, d 8",
            promocode="promo3",
            user=user,
        )

        for product in products:
            order.products.add(product)
        self.stdout.write(f"Created order {order}")
