from django import forms

from catalog.models import Product, Version


forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                           'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('creation_date', 'change_date', 'user')

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')

        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('В названии нельзя использовать слова казино, криптовалюта, крипта, биржа, '
                                            'дешево, бесплатно, обман, полиция, радар')
            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
