from django.core.management.base import BaseCommand, CommandError
import factories


class Command(BaseCommand):
    help = "Makes fake forest data for demo and testing"

    def add_arguments(self, parser):
        parser.add_argument('entries', type=int, help='Indicate how many entries to generate')

    def handle(self, *args, **options):
        try:
            factories.ForestFactory.create_batch(size=50)
        except Exception:
            raise CommandError(f'Error generating data')



