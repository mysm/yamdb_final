import csv

from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'import data from csv'

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv_file',
            type=str,
            required=True,
            help=r'path to csv file, for example .\static\data\users.csv')
        parser.add_argument(
            '--model',
            type=str,
            required=True,
            help='model name in the format application_name.model_name, \
                for example reviews.User')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        try:
            model = apps.get_model(options['model'])
        except LookupError:
            self.stdout.write(self.style.ERROR('Model not found'))
            return

        with open(csv_file, 'r', encoding='utf-8') as f:
            dr = csv.DictReader(f)
            for row in dr:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS(
            'Successfully imported data from csv'))
