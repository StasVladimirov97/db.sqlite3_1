from typing import Sequence
from django.contrib.auth.models import User
from django.core.management import BaseCommand


from shopapp.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Start demo bulk actions")
        result = Product.objects.filter(
            name__contains="Smartphone",
        ).update(discount=10)
        print(result)

        # info = [
        #     ("Smarphone 1", 199),
        #     ("Smarphone 2", 299),
        #     ("Smarphone 3", 399),
        # ]
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        # result = Product.objects.bulk_create(products)
        # for obj in result:
        #     print(obj)

        self.stdout.write("Done")
