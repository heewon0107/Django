from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : '비공개 게시글',
            }
        )
    )
    
    content = forms.CharField(
        label='Content',
        widget=forms.TextInput(
            attrs={
                'class' : 'textarea',
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
        