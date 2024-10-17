from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from .models import Meeting


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': forms.TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d and d < now().date():  # Vérifie si la date est dans le passé
            raise ValidationError("Les réunions ne peuvent pas être dans le passé.")
        return d