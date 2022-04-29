from django import forms
from .models import Link


class CreateLink(forms.ModelForm):
    long_link = forms.CharField(label='Long Link:',
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter your Link.'}))
    short_link = forms.CharField(label='Shortened Link:',
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter the shortened form '
                                                                              'of the Link (one word is allowed)'}))

    class Meta:
        model = Link
        fields = ['long_link', 'short_link']
