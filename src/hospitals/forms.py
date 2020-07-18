from django import forms
from .models import Availability


class AvailabilityModelForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ["bed_availabe"]
        widgets = {
            "bed_availabe": forms.NumberInput(attrs={"type": "tel", "size": "15"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(AvailabilityModelForm, self).__init__(*args, **kwargs)
    #     self.fields["bed_availabe"] = "Initial value"
