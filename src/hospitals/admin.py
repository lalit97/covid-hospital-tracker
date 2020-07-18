from django.contrib import admin
from .models import (
    Hospital,
    Availability,
    SearchPincode,
    SearchState,
    SearchDistrict,
    SearchTaluka,
)


class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "pincode")


class AvailabilityAdmin(admin.ModelAdmin):
    raw_id_fields = ("hospital",)


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(SearchPincode)
admin.site.register(SearchState)
admin.site.register(SearchDistrict)
admin.site.register(SearchTaluka)
