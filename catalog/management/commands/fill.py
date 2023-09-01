from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = Category.objects.all()
        categories.delete()

        category_list = [
            {'pk': '1', 'title': 'TV', 'body': ''},
            {'pk': '2', 'title': 'Smartphon', 'body': ''},
            {'pk': '3', 'title': 'Laptop', 'body': ''},
            {'pk': '4', 'title': 'keyboard', 'body': ''},
            {'pk': '5', 'title': 'PC mouse', 'body': ''}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)
