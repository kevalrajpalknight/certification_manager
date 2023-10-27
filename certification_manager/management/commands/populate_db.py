# myapp/management/commands/populate_db.py
import random
import string

from faker import Faker
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from certification_manager.models import Address, Certifications, Profession

fake = Faker()

class Command(BaseCommand):
    help = "Populate the database with dummy data"

    def add_arguments(self, parser):
        parser.add_argument(
            "number_of_records", type=int, help="Specify the number of records"
        )

    def handle(self, *args, **kwargs):
        User = get_user_model()
        number_of_records = kwargs.get("number_of_records", 1000)

        users = []
        addresses = []
        certifications = []
        professions = []

        for i in range(1, number_of_records + 1):
            user = User(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
            )
            password = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(12)
            )
            user.set_password(password)

            address = Address(
                local_address=fake.street_address(),
                city=fake.city(),
                user=user,
            )

            certification = Certifications(
                certificate_name=fake.word(),
                duration=fake.random_int(min=1, max=12),
                user=user,
            )

            profession = Profession(
                profession=fake.job(),
                user=user,
            )

            try:
                user.save()
                address.save()
                certification.save()
                profession.save()
                users.append(user)
                addresses.append(address)
                certifications.append(certification)
                professions.append(profession)
                self.stdout.write(
                    self.style.SUCCESS(f"Added record {i} of {number_of_records}")
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error adding record {i}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS(f"Added {number_of_records} records"))
