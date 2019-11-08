from django import forms
from .models import *

class AddBankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('BIC', 'name', 'master_account', 'address')
