from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):

	shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Full Name'}), required=True)
	shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Email Address'}), required=True)
	shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Address 1'}), required=True)
	shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Address 2'}), required=False)
	shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'City'}), required=True)
	shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'State'}), required=False)
	shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Zipcode'}), required=False)
	shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Country'}), required=True)
	
	class Meta:
		model = ShippingAddress
		fileds = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']
		exclude = ['user',]

class PaymentForm(forms.Form):
	card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Name on Card'}), required=True)
	card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Card Number'}), required=True)
	card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Expiration Date'}), required=True)
	card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'CVV Code'}), required=True)
	card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Billing Address 1'}), required=True)
	card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Billing Address 2'}), required=True)
	card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Billing City'}), required=True)
	card_state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Billing State'}), required=True)
	card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Billing Zipcode'}), required=True)
	card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-cnotrol', 'placeholder':'Billing Country'}), required=True)