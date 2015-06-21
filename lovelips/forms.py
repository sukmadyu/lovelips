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
    PLANNING_CHOICES_WITH_TITLES = (
        (1./5, '(1/5) Mutlak Tidak Penting Daripada'),

        (1./4, '(1/4) Sangat Tidak Penting Daripada'),

        (1./3, '(1/3) Tidak Penting Daripada'),

        (1./2, '(1/2) Tidak Cukup Penting Daripada'),

        (1, '(1) Sama Penting Daripada'),

        (2, '(2) Cukup Penting Daripada'),

        (3, '(3) Lebih Penting Daripada'),

        (4, '(4) Sangat Lebih Penting Daripada'),

        (5, '(5) Mutlak Lebih Penting Daripada'),
    )


    kri_harga_isi=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_harga_pao=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_harga_time=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_harga_cf=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_isi_pao=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_isi_time=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_isi_cf=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_pao_time=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_pao_cf=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kri_time_cf=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    class Meta:
        model = Alternatif
        fields = ('kri',)
        widgets = {
            'kri':forms.HiddenInput(),
        }
