from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = "__all__"
        widgets = {
            'location' : forms.TextInput(attrs={
                'placeholder' : "ex) 제주도"}),
            'plan' : forms.Textarea(attrs={
                'placeholder' : "ex) 슉,슈슈슉,슈슈슉"}),    
            'start_date' : forms.DateTimeInput(attrs={
                'placeholder' : "ex) 2022-02-22",}),
            'end_date' : forms.DateInput(attrs={
                'placeholder' : "ex) 2022-02-22",})
        }