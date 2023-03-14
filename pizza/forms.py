from django import forms

from .models import enqury

class enquryform(forms.ModelForm):
    class Meta:
        model=enqury
        fields=['email','username','phonenumber','message']
        labels={'Email':'email','username':'username','phonenumber':'phonenumber','message':'message'}
        
        error_messages={
            'email':{'requried':'emailrequried'},
            'username':{'requried':'username requried'},
            'phonenumber':{'requried':'phone numberrequried'},
            'message':{'requried':' messagerequried'},
        }
        widgets={'email':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
        'message':forms.TextInput(attrs={'class':'form-control'})
        }