from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string


from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Pass the number of users from 1 to 10'  # noqa(a003)

    def add_arguments(self, parser):
        parser.add_argument('num', type=int)

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        if 10 >= num >= 1:
            for i in range(num):
                username = fake.first_name()
                email = username + '@mail.com'
                password = get_random_string(8)
                User.objects.create_user(username=username, email=email, password=password)

                self.stdout.write(self.style.SUCCESS('Creating...''\n''-------------------''\n'
                                                     f'Username - "{username}"''\n'
                                                     f'Email - "{email}"''\n'
                                                     f'Password - "{password}"'))
        else:
            raise CommandError('Pass the number of users from 1 to 10')
