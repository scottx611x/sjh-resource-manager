from django.core.management import BaseCommand, CommandError

from ...models import CustomUser


class Command(BaseCommand):
    help = 'Creates a user with the specified email'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str)

    def handle(self, *args, **options):

        try:
            CustomUser.objects.create_user(options["email"])
        except Exception as e:
            raise CommandError("Something bad happened: ", e)
