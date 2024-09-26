from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = "__all__"
        widgets = {
            'memo' : forms.Textarea(attrs={'class' : 'form-control'}),
        }