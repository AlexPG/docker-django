from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from .models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            ButtonHolder(
                Submit('create', 'Create', css_class='btn-primary')
            )
        )
