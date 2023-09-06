from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = Category.objects.all()
        categories.delete()

        category_list = [
            {'pk': '1', 'title': 'Рассылки', 'body': ''},
            {'pk': '2', 'title': 'Телеграм боты', 'body': ''},
            {'pk': '3', 'title': 'Полезные утилиты', 'body': ''},
            {'pk': '4', 'title': 'Веб-приложения', 'body': ''},
            {'pk': '5', 'title': 'Микросервисы', 'body': ''}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)



