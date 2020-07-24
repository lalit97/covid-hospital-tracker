import os
import csv
from django.conf import settings
from hospitals.models import Hospital
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "uploading result"

    def handle(self, *args, **options):
        filename = "data.csv"
        path = os.path.join(settings.PROJECT_PATH, filename)
        file = open(path, "r")
        reader = csv.DictReader(file)
        for dict_ in reader:
            name = dict_["Health Facility Name"]
            address = dict_["Address"]
            street = dict_["street"]
            landmark = dict_["landmark"]
            locality = dict_["locality"]
            pincode = dict_["pincode"]
            try:
                int(pincode)
            except:
                pincode = None
            landline = dict_["landline_number"]
            latitude = dict_["latitude"]
            try:
                float(latitude)
            except:
                latitude = None
            longitude = dict_["longitude"]
            try:
                float(longitude)
            except:
                longitude = None
            altitude = dict_["altitude"]
            try:
                float(altitude)
            except:
                altitude = None
            facility_type = dict_["Facility Type"]
            state = dict_["State_Name"]
            district = dict_["District_Name"]
            taluka = dict_["Taluka_Name"]
            block = dict_["Block_Name"]
            try:
                Hospital.objects.get_or_create(
                    name=name,
                    address=address,
                    street=street,
                    landmark=landmark,
                    locality=locality,
                    pincode=pincode,
                    landline=landline,
                    latitude=latitude,
                    longitude=longitude,
                    altitude=altitude,
                    facility_type=facility_type,
                    state=state,
                    district=district,
                    taluka=taluka,
                    block=block,
                )
            except Exception as e:
                print(e)
