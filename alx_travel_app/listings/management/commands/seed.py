# listings/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Optional: Clear existing listings
        Listing.objects.all().delete()
        self.stdout.write(self.style.WARNING("Deleted old listings."))

        # Create or get a default user
        user, created = User.objects.get_or_create(username='demo_user')
        if created:
            user.set_password('password123')
            user.save()

        # Create 10 sample listings
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.paragraph(nb_sentences=5),
                price_per_night=random.uniform(50, 300),
                location=fake.city(),
                owner=user
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
