from django import forms

from .models import userInput

class InputForm(forms.ModelForm):
	class Meta:
		model=userInput
		fields=('first','second','ifile',)