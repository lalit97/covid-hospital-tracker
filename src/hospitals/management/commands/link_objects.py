from tqdm import tqdm
from django.core.management.base import BaseCommand, CommandError
from hospitals.models import (
    Hospital,
    SearchState,
    SearchDistrict,
    SearchTaluka
)


class Command(BaseCommand):
    help = "linking objects"

    def handle(self, *args, **options):
        """
        link State, District and Taluka Objects
        """
        items = Hospital.objects.values_list(
            'state', 'district', 'taluka').distinct()
        for state, district, taluka in tqdm(items):
            if taluka != '' and district != '':
                state, _ = SearchState.objects.get_or_create(state=state)
                district, _ = SearchDistrict.objects.get_or_create(
                    district=district)
                district.state = state
                district.save()
                taluka, _ = SearchTaluka.objects.get_or_create(taluka=taluka)
                taluka.district = district
                taluka.state = state
                taluka.save()
