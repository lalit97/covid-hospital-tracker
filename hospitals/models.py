from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=400, blank=True)
    address = models.CharField(max_length=400, blank=True)
    street = models.CharField(max_length=400, blank=True)
    landmark = models.CharField(max_length=400, blank=True)
    locality = models.CharField(max_length=400, blank=True)
    pincode = models.IntegerField(blank=True, null=True)
    landline = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    facility_type = models.CharField(max_length=400, blank=True)
    state = models.CharField(max_length=400, blank=True)
    district = models.CharField(max_length=400, blank=True)
    taluka = models.CharField(max_length=400, blank=True)
    block = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return str(self.name)


class Availability(models.Model):
    bed_availabe = models.IntegerField(blank=True, null=True, default=0)
    hospital = models.OneToOneField(Hospital, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bed_availabe)


class SearchPincode(models.Model):
    pincode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.pincode)


class SearchState(models.Model):
    state = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return str(self.state)


class SearchDistrict(models.Model):
    state = models.ForeignKey(SearchState, on_delete=models.CASCADE, null=True)
    district = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return str(self.district)


class SearchTaluka(models.Model):
    state = models.ForeignKey(SearchState, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(SearchDistrict, on_delete=models.CASCADE, null=True)
    taluka = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return str(self.taluka)
