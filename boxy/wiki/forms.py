from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'create/'
        self.helper.add_input(Submit('submit', 'Submit'))
