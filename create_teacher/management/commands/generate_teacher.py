from django.core.management.base import BaseCommand
from create_teacher.models import Teacher

import faker

fake = faker.Faker()


class Command(BaseCommand):
    help = "Add the specified number of teachers to database"

    def add_arguments(self, parser):
        parser.add_argument(
            "number",
            type=int,
            nargs="?",
            default=100,
            help="Number of teachers to add (default is 100)",
        )

    def handle(self, *args, **options):
        for i in range(options["number"]):
            t = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                subject=fake.job(),
                birth_date=fake.date_of_birth(),
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % t.id)
            )
