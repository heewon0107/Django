from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : '메뉴 이름을 작성해주세요.'
            })
    

    )
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'description' : forms.Textarea(
                attrs={
                    'placeholder' : '메뉴 설명을 작성해 주세요.'
                }) 
        }