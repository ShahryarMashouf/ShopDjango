from django import forms
from .models import UserComments

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1)
    product_id = forms.IntegerField(widget=forms.HiddenInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        fields = '__all__'
        