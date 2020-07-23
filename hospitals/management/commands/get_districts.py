from hospitals.models import Hospital, SearchDistrict
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "getting districts"

    def handle(self, *args, **options):
        districts = Hospital.objects.values_list(
            'district', flat=True).distinct()
        for district in districts:
            try:
                if district != '':
                    SearchDistrict.objects.create(district=district)
            except Exception as e:
                print(e)
