from hospitals.models import SearchPincode, Hospital
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "getting pincodes"

    def handle(self, *args, **options):
        pincodes = Hospital.objects.values_list(
            'pincode', flat=True).distinct()
        for pincode in pincodes:
            try:
                if pincodes is not None and pincode != '':
                    SearchPincode.objects.create(pincode=pincode)
            except Exception as e:
                print(e)
