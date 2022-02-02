from django import forms

from .models import *

from .models import Category

from .models import Category, Order


class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False) 
	
class AccountForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Leave blank if no change'}), required=False)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Leave blank if no change'}), required=False)
	password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Leave blank if no change'}), required=False)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mimage = forms.CharField(widget=forms.FileInput(attrs={'class':'form-control image-input', 'accept': 'image/*', 'multiple': 'multiple'}), required=False)
	phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
	about_me = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id': 'ck-editor-area'}), required=False)
	
class CreateProductForm(forms.Form):
	
	# category = forms.CharField(widget=forms.Select(choices=Category.Category_Choices, attrs={'class':'form-control'})	)
	category = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id': 'ck-editor-area'}))
	excerpt = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows': '7'}), required=False)
	price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Amount'}))
	status = forms.CharField(widget=forms.Select(choices=(('1', 'Active'),('0', 'Inactive'),), attrs={'class':'form-control'}))
	quantity = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	# class meta:
	# 	for cat in Category.objects.all():
	# 		p_cat = cat

	
class UpdateProductForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'id': 'ck-editor-area'}))
	excerpt = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows': '7'}), required=False)
	images = forms.CharField(widget=forms.FileInput(attrs={'class':'form-control image-input', 'accept': 'image/*', 'multiple': 'multiple'}), required=False)
	price = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Amount'}))
	status = forms.CharField(widget=forms.Select(choices=(('1', 'Active'),('0', 'Inactive'),), attrs={'class':'form-control'}))
	quantity = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    
class MemberForm(forms.ModelForm):
  
    class Meta:
        model = Member
        fields = ['mimage']

class CheckoutForm(forms.ModelForm):
	# first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='First name')
	# last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Last name')
	# email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), label='E-mail Address')
	# phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Telephone')
	# address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Address')
	# city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='City')
	# zip_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='ZIP code')
	# state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='State')
	# order_notes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='order_notes')

	# delivery_method = forms.CharField(required=True)
	# payment_method = forms.CharField(required=True)
	class Meta:
		model = Order
		fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city',
				  'zip_code', 'state', 'payment_method', 'order_notes')

	# quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	# update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
