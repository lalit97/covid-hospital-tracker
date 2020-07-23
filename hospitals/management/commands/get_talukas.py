from hospitals.models import Hospital, SearchTaluka
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "getting talukas"

    def handle(self, *args, **options):
        talukas = Hospital.objects.values_list(
            'taluka', flat=True).distinct()
        for taluka in talukas:
            try:
                if taluka != '':
                    SearchTaluka.objects.create(taluka=taluka)
            except Exception as e:
                print(e)
