from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not title.endswith("jj"):
            raise forms.ValidationError("Invalid title.")
        return title
