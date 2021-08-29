import datetime

from django.forms import *

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import DataTemplate

GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)
subjects = (('gardening','gardening'),( 'home', 'home'), ('learning','learning'))


class TemplateForm(ModelForm):

    subject = ChoiceField(label='', choices=subjects)

    sub_subject = CharField(max_length=30)
    template = Textarea()

    def clean_subject(self):
        data = self.cleaned_data['subject']
        # Remember to always return the cleaned data.
        return data

    def clean_sub_subject(self):
        data = self.cleaned_data['sub_subject']
        # Remember to always return the cleaned data.
        return data

    def clean_template(self):
        data = self.cleaned_data['template']
        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = DataTemplate
        fields = ('subject', 'sub_subject', 'template')
        widgets = {
            'subject': Select(attrs={'class': 'regDropDown'}),
            # 'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'style': 'width: 50px;', 'class': 'form-control'}),
            'sub_subject': TextInput(attrs={'placeholder': 'Sub Subject', 'class': 'form-control'}),
            'template': Textarea(attrs={'placeholder': 'Template in Json format', 'class': 'form-control'}),
        }
