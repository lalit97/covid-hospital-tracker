from hospitals.models import Hospital, SearchState
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "getting pincodes"

    def handle(self, *args, **options):
        states = Hospital.objects.values_list('state', flat=True).distinct()
        for state in states:
            try:
                SearchState.objects.create(state=state)
            except Exception as e:
                print(e)
