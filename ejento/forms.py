from django import forms



from .models import *

class KontakForm(forms.ModelForm):

    class Meta:
		model = Komentar
		fields = ('nama','email','pesan',)
		widgets = {
			'nama': forms.TextInput(attrs={'id':'icon_prefix','type':'text','class':'validate white-text','placeholder':'Your Name *','data-validation-required-message':'Please enter your name.'}),
			'email': forms.EmailInput(attrs={'id':'icon_email','type':'text','class':'validate white-text','placeholder':'Your Email *','data-validation-required-message':'Please enter your email.'}),
			'pesan': forms.Textarea(attrs={'id':'icon_prefix2','type':'text','class':'materialize-textarea white-text','style':'height: 85px;','placeholder':'Your Message *','data-validation-required-message':'Please enter your message.'}),
			}

class NamaAgenForm(forms.ModelForm):

    agen_a=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    agen_b=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    agen_c=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    class Meta:
        model = Alternatif
        fields = ('nama_agen',)
        widgets = {

            'nama_agen':forms.HiddenInput(),
        }

class AHPForm(forms.ModelForm):

    pp_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    pp_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    pp_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    up_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    up_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    up_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    sp_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    sp_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    sp_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':''}))
    class Meta:
        model = Alternatif
        fields = ('pp','up','sp')
        widgets = {

            'pp':forms.HiddenInput(),
            'up':forms.HiddenInput(),
            'sp':forms.HiddenInput(),
        }
class AHPKriteriaForm(forms.ModelForm):

    kri_pp_up=forms.FloatField()
    kri_pp_sp=forms.FloatField()
    kri_up_sp=forms.FloatField()
    class Meta:
        model = Alternatif
        fields = ('kri',)
        widgets = {
            'kri':forms.HiddenInput(),
        }
