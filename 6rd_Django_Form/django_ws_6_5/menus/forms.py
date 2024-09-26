from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        CHOICES = [(True, 'YES'), (False, 'NO')]
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                    }
                ),
            'is_vegan': forms.RadioSelect(attrs={'class': 'form-check'}, choices=CHOICES),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        
        }
        error_messages = {
            'price' : {
                'invalid' : '올바른 가격을 입력해 주세요. ex)12.34',
                'max_decimal_places' : '가격은 최대 8자리였숴',
                'max_digits' : '가격음메 소수점 이하 두자리 ㄱㄱ',
            }
        }