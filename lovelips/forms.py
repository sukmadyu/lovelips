from django import forms



from .models import *

class KontakForm(forms.ModelForm):

    class Meta:
		model = Komentar
		fields = ('nama','email','no_telepon','pesan',)
		widgets = {
			'nama': forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Your Name *','data-validation-required-message':'Please enter your name.'}),
			'email': forms.EmailInput(attrs={'type':'text','class':'form-control','placeholder':'Your Email *','data-validation-required-message':'Please enter your email.'}),
			'no_telepon': forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Your Phone Number *','data-validation-required-message':'Please enter your phone number.'}),
			'pesan': forms.Textarea(attrs={'type':'text','class':'form-control','placeholder':'Your Message *','data-validation-required-message':'Please enter your message.'}),
			}

class NamaProdukForm(forms.ModelForm):

    produk_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control '}))
    produk_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    produk_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Alternatif
        fields = ('nama_product',)
        widgets = {

            'nama_product':forms.HiddenInput(),
        }

class AHPForm(forms.ModelForm):

    harga_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control '}))
    harga_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    harga_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    isi_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    isi_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    isi_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pao_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pao_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pao_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    time_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    time_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    time_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cruelty_free_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cruelty_free_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cruelty_free_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Alternatif
        fields = ('harga','isi','pao','time','cruelty_free')
        widgets = {

            'harga':forms.HiddenInput(),
            'isi':forms.HiddenInput(),
            'pao':forms.HiddenInput(),
	    'time':forms.HiddenInput(),
	    'cruelty_free':forms.HiddenInput(),
        }
class AHPKriteriaForm(forms.ModelForm):

    kri_harga_isi=forms.FloatField()
    kri_harga_pao=forms.FloatField()
    kri_harga_time=forms.FloatField()
    kri_harga_cf=forms.FloatField()
    kri_isi_pao=forms.FloatField()
    kri_isi_time=forms.FloatField()
    kri_isi_cf=forms.FloatField()
    kri_pao_time=forms.FloatField()
    kri_pao_cf=forms.FloatField()
    kri_time_cf=forms.FloatField()
    class Meta:
        model = Alternatif
        fields = ('kri',)
        widgets = {
            'kri':forms.HiddenInput(),
        }
