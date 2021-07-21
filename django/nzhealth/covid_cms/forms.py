from django import forms  
from covid_cms.models import Referral  
class ReferralForm(forms.ModelForm):  
    class Meta:  
        model = Referral  
        fields = "__all__"  