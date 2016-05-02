import simplejson as json
import numpy as np
from numpy import linalg as LA
from decimal import Decimal as D

from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView


from .forms import *
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

class HomeView(View):
    template_name = 'index.html'
    def get(self,request):

        form = KontakForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):

        form = KontakForm(request.POST or None)
        if form.is_valid():
            kontak=form.save(commit=False)
            kontak.save()
	    subject= 'Pesan pada website Ejento dari {}'.format(kontak.nama)
	    message= 'nama: {} \nemail: {} \nno telepon: {} \nmessage: {}'.format(kontak.nama,kontak.email,kontak.no_telepon,kontak.pesan)
	    email_from= settings.EMAIL_HOST_USER
	    email_to= 'sukmadyu@gmail.com'
	    send_mail(subject, message, email_from, [email_to], fail_silently=False)
            messages.success(request,'Your comment has been successfully saved')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'An error has occured, please try again')
            return render(request,self.template_name,{'form':form})

class InputKriteriaAHPView(View):
    template_name = 'ahp/input-kri.html'
    def get(self,request):

        form = AHPKriteriaForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):

        form = AHPKriteriaForm(request.POST or None)
        if form.is_valid():
            ahp=form.save(commit=False)
            kri_pp_up=form.cleaned_data['kri_pp_up']
            kri_pp_sp=form.cleaned_data['kri_pp_sp']
            kri_up_sp=form.cleaned_data['kri_up_sp']
            kriteria=[]
            kriteria.append(kri_pp_up),kriteria.append(kri_pp_sp)
            kriteria.append(kri_up_sp)
            ahp.kri= json.dumps(kriteria)
            ahp.save()
            messages.success(request,'Input nilai perbandingan kriteria telah berhasil')
            return HttpResponseRedirect(reverse('konsistensi-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'Ada kesalahan yang terjadi, mohon ulangi lagi')
            return render(request,self.template_name,{'form':form})

class InputAHPView(View):
    template_name = 'ahp/input-ahp.html'
    id = None
    def get(self, request, id):
        ahp = Alternatif.objects.get(id=id)
        form = AHPForm(instance=ahp)
	jsonDec = json.decoder.JSONDecoder()


        nama = jsonDec.decode(ahp.nama_agen)
        nama_a=nama[0]
        nama_b=nama[1]
        nama_c=nama[2]


        return render(request,self.template_name,{'form':form,'ahp':ahp,
						   'nama_a':nama_a,'nama_b':nama_b,'nama_c':nama_c,
							})

    def post(self, request, id=None):
        ahp_ob = Alternatif.objects.get(id=id)
        form = AHPForm(request.POST, instance=ahp_ob)
        if form.is_valid():
	    
            ahp=form.save(commit=False)
            pp_a=form.cleaned_data['pp_a']
            pp_b=form.cleaned_data['pp_b']
            pp_c=form.cleaned_data['pp_c']
            pp=[]
            pp.append(pp_a),pp.append(pp_b),pp.append(pp_c)
            ahp.pp= json.dumps(pp)
            up_a=form.cleaned_data['up_a']
            up_b=form.cleaned_data['up_b']
            up_c=form.cleaned_data['up_c']
            up=[]
            up.append(up_a),up.append(up_b),up.append(up_c)
            ahp.up= json.dumps(up)
            sp_a=form.cleaned_data['sp_a']
            sp_b=form.cleaned_data['sp_b']
            sp_c=form.cleaned_data['sp_c']
            sp=[]
            sp.append(sp_a),sp.append(sp_b),sp.append(sp_c)
            ahp.sp= json.dumps(sp)
            ahp.save()
            messages.success(request,'Input data agen berhasil')
            return HttpResponseRedirect(reverse('detail-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'Kesalahan dalam input data agen, mohon ulangi lagi')
            return render(request,self.template_name,{'form':form})

RI = (0, 0, D('0.58'), D('0.9'), D('1.12'),
      D('1.24'), D('1.32'), D('1.41'), D('1.45'), D('1.49'),
      D('1.51'), D('1.48'), D('1.56'), D('1.57'), D('1.59')
)
def calculateConsistency(arr):

   eva = max(LA.eig(arr)[0]).real
   n = len(arr)
   CI = (eva-n) / (n-1)

   return CI / float(RI[n])


def calculateWeights(arr, rounding=4):

   PLACES = D(10) ** -(rounding)
   evas, eves = LA.eig(arr)
   eva = max(evas)
   eva_idx = evas.tolist().index(eva)
   eve = eves.take((eva_idx,), axis=1)
   normalized = eve / sum(eve)
   vector = [abs(e[0]) for e in normalized]
   arr= [ D( v ).quantize(PLACES) for v in vector ]
   return arr

def calculateWeightsmin(arr, rounding=4):

   PLACES = D(10) ** -(rounding)
   evas, eves = LA.eig(arr)
   eva = min(evas)
   eva_idx = evas.tolist().index(eva)
   eve = eves.take((eva_idx,), axis=1)
   normalized = eve / sum(eve)
   vector = [abs(e[0]) for e in normalized]
   arr= [ D( v ).quantize(PLACES) for v in vector ]
   return arr

class DetailAHPView(View):
    template_name = 'ahp/hasil-ahp.html'
    id = None
    def get(self,request,id=None):
        alternatif = Alternatif.objects.get(id=id)
        jsonDec = json.decoder.JSONDecoder()
        nama = jsonDec.decode(alternatif.nama_agen)
        nama_a=nama[0]
        nama_b=nama[1]
        nama_c=nama[2]

        pp = jsonDec.decode(alternatif.pp)
        pp_a=float(pp[0])
        pp_b=float(pp[1])
        pp_c=float(pp[2])
        pp_arr=np.array([pp_a/pp_a,pp_b/pp_a,pp_c/pp_a,
                            pp_a/pp_b,pp_b/pp_b,pp_c/pp_b,
                            pp_a/pp_c,pp_b/pp_c,pp_c/pp_c])
        pp_arr=pp_arr.reshape(3,3)

        pp_arr=calculateWeights(pp_arr)

        pp_arr_a=pp_arr[0]
        pp_arr_b=pp_arr[1]
        pp_arr_c=pp_arr[2]

        pp_arr=np.array(pp_arr)
        pp_arr=pp_arr.reshape(3,1)


        up = jsonDec.decode(alternatif.up)
        up_a=float(up[0])
        up_b=float(up[1])
        up_c=float(up[2])
        up_arr=np.array([up_a/up_a,up_b/up_a,up_c/up_a,
                          up_a/up_b,up_b/up_b,up_c/up_b,
                          up_a/up_c,up_b/up_c,up_c/up_c])
        up_arr=up_arr.reshape(3,3)

        up_arr=calculateWeights(up_arr)
        up_arr_a=up_arr[0]
        up_arr_b=up_arr[1]
        up_arr_c=up_arr[2]

        up_arr=np.array(up_arr)
        up_arr=up_arr.reshape(3,1)

        sp = jsonDec.decode(alternatif.sp)
        sp_a=float(sp[0])
        sp_b=float(sp[1])
        sp_c=float(sp[2])
        sp_arr=np.array([sp_a/sp_a,sp_b/sp_a,sp_c/sp_a,
                          sp_a/sp_b,sp_b/sp_b,sp_c/sp_b,
                          sp_a/sp_c,sp_b/sp_c,sp_c/sp_c])
        sp_arr=sp_arr.reshape(3,3)

        sp_arr=calculateWeights(sp_arr)

        sp_arr_a=sp_arr[0]
        sp_arr_b=sp_arr[1]
        sp_arr_c=sp_arr[2]

        sp_arr=np.array(sp_arr)
        sp_arr=sp_arr.reshape(3,1)

        kri = jsonDec.decode(alternatif.kri)
        kri_a=float(kri[0])
        kri_b=float(kri[1])
        kri_c=float(kri[2])
	kri_d=float(kri[3])
	kri_e=float(kri[4])
	kri_f=float(kri[5])
	kri_g=1/kri_a
	kri_h=1/kri_b
	kri_i=1/kri_d
	kri_j=1/kri_c
	kri_k=1/kri_e
	kri_l=1/kri_f

        kri_arr=np.array([1,kri_a,kri_b,kri_c,
                          1/kri_a,1,kri_d,kri_e,
                          1/kri_b,1/kri_d,1,kri_f,
                          1/kri_c,1/kri_e,1/kri_f,1])
        kri_arr=kri_arr.reshape(4,4)
        cons=calculateConsistency(kri_arr)


        kri_arr=calculateWeights(kri_arr)
	kri_pp=kri_arr[0]
        kri_up=kri_arr[1]
        kri_sp=kri_arr[2]

        kri_arr=np.array(kri_arr)
        kri_arr=kri_arr.reshape(3,1)

        alt=np.concatenate((pp_arr, up_arr), axis=1)
	alt=np.concatenate((alt, sp_arr), axis=1)
        alt=alt.reshape(3,3)
        hasil=np.dot(alt,kri_arr)

        agen_a=float(hasil[0])
        agen_b=float(hasil[1])
        agen_c=float(hasil[2])

        maks=np.amax(hasil)
        maks=np.array(maks)
        hasil=hasil.tolist()
        inde=hasil.index(maks)
        agen=[nama_a,nama_b, nama_c]

        return render(request,self.template_name,{'pp_a':int(pp_a),'pp_b':int(pp_b),'pp_c':int(pp_c),
                                                  'up_a':int(up_a),'up_b':int(up_b),'up_c':int(up_c),
                                                  'sp_a':int(sp_a),'sp_b':int(sp_b),'sp_c':int(sp_c),
                                                  'bobot_pp_a':pp_arr_a,'bobot_pp_b':pp_arr_b,'bobot_pp_c':pp_arr_c,
                                                  'bobot_up_a':up_arr_a,'bobot_up_b':up_arr_b,'bobot_up_c':up_arr_c,
                                                  'bobot_sp_a':sp_arr_a,'bobot_sp_b':sp_arr_b,'bobot_sp_c':sp_arr_c,
                                                  'kri_a':kri_a,'kri_b':kri_b,'kri_c':kri_c,
						  'kri_d':kri_d,'kri_e':kri_e,'kri_e':kri_e,'kri_f':kri_f,
						  'kri_g':kri_g,'kri_h':kri_h,'kri_i':kri_i,
						  'kri_j':kri_j,'kri_k':kri_k,'kri_l':kri_l,                                                
						  'bobot_pp':kri_pp,'bobot_up':kri_up,'bobot_sp':kri_sp,
                                                  'agen_a':agen_a,'agen_b':agen_b,'agen_c':agen_c,
                                                  'agen_max':agen[inde],'cons':cons,'cons_pre':cons*100,
                                                  'nama_a':nama_a,'nama_b':nama_b,'nama_c':nama_c,  
                                                    })
class KonsistensiAHPView(View):
    template_name = 'ahp/konsistensi-ahp.html'
    id = None
    def get(self,request,id=None):
        alternatif = Alternatif.objects.get(id=id)
        jsonDec = json.decoder.JSONDecoder()

        kri = jsonDec.decode(alternatif.kri)
        kri_a=float(kri[0])
        kri_b=float(kri[1])
        kri_c=float(kri[2])
	kri_d=float(kri[3])
	kri_e=float(kri[4])
	kri_f=float(kri[5])
	kri_g=1/kri_a
	kri_h=1/kri_b
	kri_i=1/kri_d
	kri_j=1/kri_c
	kri_k=1/kri_e
	kri_l=1/kri_f

        kri_arr=np.array([1,kri_a,kri_b,kri_c,
                          1/kri_a,1,kri_d,kri_e,
                          1/kri_b,1/kri_d,1,kri_f,
                          1/kri_c,1/kri_e,1/kri_f,1])
        kri_arr=kri_arr.reshape(4,4)
        cons=calculateConsistency(kri_arr)


        kri_arr=calculateWeights(kri_arr)
	kri_pp=kri_arr[0]
        kri_up=kri_arr[1]
        kri_sp=kri_arr[2]

        kri_arr=np.array(kri_arr)
        kri_arr=kri_arr.reshape(3,1)

        return render(request,self.template_name,{'kri_a':kri_a,'kri_b':kri_b,'kri_c':kri_c,
						'kri_d':kri_d,'kri_e':kri_e,'kri_e':kri_e,'kri_f':kri_f,
						'kri_g':kri_g,'kri_h':kri_h,'kri_i':kri_i,
						'kri_j':kri_j,'kri_k':kri_k,'kri_l':kri_l,
						'bobot_pp':kri_pp,'bobot_up':kri_up,'bobot_sp':kri_sp,
						'cons':cons,'cons_pre':cons*100,'alternatif':alternatif
						})

class InputNamaView(View):
    template_name = 'ahp/input-nama.html'
    id = None
    def get(self, request, id):
        ahp = Alternatif.objects.get(id=id)
        form = NamaAgenForm(instance=ahp)
        return render(request,self.template_name,{'form':form,'ahp':ahp})

    def post(self, request, id=None):
        ahp_ob = Alternatif.objects.get(id=id)
        form = NamaAgenForm(request.POST, instance=ahp_ob)
        if form.is_valid():
            ahp=form.save(commit=False)
            agen_a=form.cleaned_data['agen_a']
            agen_b=form.cleaned_data['agen_b']
            agen_c=form.cleaned_data['agen_c']
            agen=[]
            agen.append(agen_a),agen.append(agen_b),agen.append(agen_c)
            ahp.nama_agen= json.dumps(agen)
            ahp.save()
            messages.success(request,'Input nama agen telah berhasil')
            return HttpResponseRedirect(reverse('input-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'Ada kesalahan saaat input nama agen, mohon ulangi lagi')
            return render(request,self.template_name,{'form':form})