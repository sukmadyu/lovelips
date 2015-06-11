import simplejson as json
import numpy as np
from numpy import linalg as LA
from decimal import Decimal as D


from django.contrib import messages
from django.core.urlresolvers import reverse
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
            kri_harga_isi=form.cleaned_data['kri_harga_isi']
            kri_harga_pao=form.cleaned_data['kri_harga_pao']
            kri_harga_time=form.cleaned_data['kri_harga_time']
            kri_harga_cf=form.cleaned_data['kri_harga_cf']
            kri_isi_pao=form.cleaned_data['kri_isi_pao']
            kri_isi_time=form.cleaned_data['kri_isi_time']
            kri_isi_cf=form.cleaned_data['kri_isi_cf']
            kri_pao_time=form.cleaned_data['kri_pao_time']
            kri_pao_cf=form.cleaned_data['kri_pao_cf']
            kri_time_cf=form.cleaned_data['kri_time_cf']
            kriteria=[]
            kriteria.append(kri_harga_isi),kriteria.append(kri_harga_pao),kriteria.append(kri_harga_time),kriteria.append(kri_harga_cf)
            kriteria.append(kri_isi_pao),kriteria.append(kri_isi_time),kriteria.append(kri_isi_cf)
            kriteria.append(kri_pao_time),kriteria.append(kri_pao_cf)
            kriteria.append(kri_time_cf)
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


        nama = jsonDec.decode(ahp.nama_product)
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
            harga_a=form.cleaned_data['harga_a']
            harga_b=form.cleaned_data['harga_b']
            harga_c=form.cleaned_data['harga_c']
            harga=[]
            harga.append(harga_a),harga.append(harga_b),harga.append(harga_c)
            ahp.harga= json.dumps(harga)
            isi_a=form.cleaned_data['isi_a']
            isi_b=form.cleaned_data['isi_b']
            isi_c=form.cleaned_data['isi_c']
            isi=[]
            isi.append(isi_a),isi.append(isi_b),isi.append(isi_c)
            ahp.isi= json.dumps(isi)
            pao_a=form.cleaned_data['pao_a']
            pao_b=form.cleaned_data['pao_b']
            pao_c=form.cleaned_data['pao_c']
            pao=[]
            pao.append(pao_a),pao.append(pao_b),pao.append(pao_c)
            ahp.pao= json.dumps(pao)
	    time_a=form.cleaned_data['time_a']
            time_b=form.cleaned_data['time_b']
            time_c=form.cleaned_data['time_c']
            time=[]
            time.append(time_a),time.append(time_b),time.append(time_c)
            ahp.time= json.dumps(time)
	    cruelty_free_a=form.cleaned_data['cruelty_free_a']
            cruelty_free_b=form.cleaned_data['cruelty_free_b']
            cruelty_free_c=form.cleaned_data['cruelty_free_c']
            cruelty_free=[]
            cruelty_free.append(cruelty_free_a),cruelty_free.append(cruelty_free_b),cruelty_free.append(cruelty_free_c)
            ahp.cruelty_free= json.dumps(cruelty_free)
            ahp.save()
            messages.success(request,'Input data produk berhasil')
            return HttpResponseRedirect(reverse('detail-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'Kesalahan dalam input data produk, mohon ulangi lagi')
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
        nama = jsonDec.decode(alternatif.nama_product)
        nama_a=nama[0]
        nama_b=nama[1]
        nama_c=nama[2]

        harga = jsonDec.decode(alternatif.harga)
        harga_a=float(harga[0])
        harga_b=float(harga[1])
        harga_c=float(harga[2])
        harga_arr=np.array([harga_a/harga_a,harga_b/harga_a,harga_c/harga_a,
                            harga_a/harga_b,harga_b/harga_b,harga_c/harga_b,
                            harga_a/harga_c,harga_b/harga_c,harga_c/harga_c])
        harga_arr=harga_arr.reshape(3,3)

        harga_arr=calculateWeights(harga_arr)

        harga_arr_a=harga_arr[0]
        harga_arr_b=harga_arr[1]
        harga_arr_c=harga_arr[2]

        harga_arr=np.array(harga_arr)
        harga_arr=harga_arr.reshape(3,1)


        isi = jsonDec.decode(alternatif.isi)
        isi_a=float(isi[0])
        isi_b=float(isi[1])
        isi_c=float(isi[2])
        isi_arr=np.array([isi_a/isi_a,isi_b/isi_a,isi_c/isi_a,
                          isi_a/isi_b,isi_b/isi_b,isi_c/isi_b,
                          isi_a/isi_c,isi_b/isi_c,isi_c/isi_c])
        isi_arr=isi_arr.reshape(3,3)

        isi_arr=calculateWeights(isi_arr)
        isi_arr_a=isi_arr[0]
        isi_arr_b=isi_arr[1]
        isi_arr_c=isi_arr[2]

        isi_arr=np.array(isi_arr)
        isi_arr=isi_arr.reshape(3,1)

        pao = jsonDec.decode(alternatif.pao)
        pao_a=float(pao[0])
        pao_b=float(pao[1])
        pao_c=float(pao[2])
        pao_arr=np.array([pao_a/pao_a,pao_b/pao_a,pao_c/pao_a,
                          pao_a/pao_b,pao_b/pao_b,pao_c/pao_b,
                          pao_a/pao_c,pao_b/pao_c,pao_c/pao_c])
        pao_arr=pao_arr.reshape(3,3)

        pao_arr=calculateWeights(pao_arr)

        pao_arr_a=pao_arr[0]
        pao_arr_b=pao_arr[1]
        pao_arr_c=pao_arr[2]

        pao_arr=np.array(pao_arr)
        pao_arr=pao_arr.reshape(3,1)

	time = jsonDec.decode(alternatif.time)
        time_a=float(time[0])
        time_b=float(time[1])
        time_c=float(time[2])
        time_arr=np.array([time_a/time_a,time_b/time_a,time_c/time_a,
                           time_a/time_b,time_b/time_b,time_c/time_b,
                           time_a/time_c,time_b/time_c,time_c/time_c])
        time_arr=time_arr.reshape(3,3)

        time_arr=calculateWeights(time_arr)

        time_arr_a=time_arr[0]
        time_arr_b=time_arr[1]
        time_arr_c=time_arr[2]

        time_arr=np.array(time_arr)
        time_arr=time_arr.reshape(3,1)

	cruelty_free = jsonDec.decode(alternatif.cruelty_free)
        cruelty_free_a=float(cruelty_free[0])
        cruelty_free_b=float(cruelty_free[1])
        cruelty_free_c=float(cruelty_free[2])
        cruelty_free_arr=np.array([cruelty_free_a/cruelty_free_a,cruelty_free_b/cruelty_free_a,cruelty_free_c/cruelty_free_a,
                                   cruelty_free_a/cruelty_free_b,cruelty_free_b/cruelty_free_b,cruelty_free_c/cruelty_free_b,
                                   cruelty_free_a/cruelty_free_c,cruelty_free_b/cruelty_free_c,cruelty_free_c/cruelty_free_c])
        cruelty_free_arr=cruelty_free_arr.reshape(3,3)

        cruelty_free_arr=calculateWeights(cruelty_free_arr)

        cruelty_free_arr_a=cruelty_free_arr[0]
        cruelty_free_arr_b=cruelty_free_arr[1]
        cruelty_free_arr_c=cruelty_free_arr[2]

        cruelty_free_arr=np.array(cruelty_free_arr)
        cruelty_free_arr=cruelty_free_arr.reshape(3,1)

        kri = jsonDec.decode(alternatif.kri)
        kri_a=float(kri[0])
        kri_b=float(kri[1])
        kri_c=float(kri[2])
	kri_d=float(kri[3])
	kri_e=float(kri[4])
	kri_f=float(kri[5])
	kri_g=float(kri[6])
	kri_h=float(kri[7])
	kri_i=float(kri[8])
	kri_j=float(kri[9])
        kri_arr=np.array([1,kri_a,kri_b,kri_c,kri_d,
                          1/kri_a,1,kri_e,kri_f,kri_g,
                          1/kri_b,1/kri_e,1,kri_h,kri_i,
			  1/kri_c,1/kri_f,1/kri_h,1,kri_j,
                          1/kri_d,1/kri_g,1/kri_i,1/kri_j,1])
        kri_arr=kri_arr.reshape(5,5)
        cons=calculateConsistency(kri_arr)


        kri_arr=calculateWeights(kri_arr)
	kri_harga=kri_arr[0]
        kri_isi=kri_arr[1]
        kri_pao=kri_arr[2]
        kri_time=kri_arr[3]
	kri_cruelty_free=kri_arr[4]

        kri_arr=np.array(kri_arr)
        kri_arr=kri_arr.reshape(5,1)

        alt=np.concatenate((harga_arr, isi_arr), axis=1)
	alt=np.concatenate((alt, pao_arr), axis=1)
        alt=np.concatenate((alt, time_arr), axis=1) 
	alt=np.concatenate((alt, cruelty_free_arr), axis=1)
        alt=alt.reshape(3,5)
        hasil=np.dot(alt,kri_arr)

        produk_a=float(hasil[0])
        produk_b=float(hasil[1])
        produk_c=float(hasil[2])

        maks=np.amax(hasil)
        maks=np.array(maks)
        hasil=hasil.tolist()
        inde=hasil.index(maks)
        produk=[nama_a,nama_b, nama_c]

        return render(request,self.template_name,{'harga_a':int(harga_a),'harga_b':int(harga_b),'harga_c':int(harga_c),
                                                  'isi_a':int(isi_a),'isi_b':int(isi_b),'isi_c':int(isi_c),
                                                  'pao_a':int(pao_a),'pao_b':int(pao_b),'pao_c':int(pao_c),
						  'time_a':int(time_a),'time_b':int(time_b),'time_c':int(time_c),
						  'cruelty_free_a':int(cruelty_free_a),'cruelty_free_b':int(cruelty_free_b),'cruelty_free_c':int(cruelty_free_c),
                                                  'bobot_harga_a':harga_arr_a,'bobot_harga_b':harga_arr_b,'bobot_harga_c':harga_arr_c,
                                                  'bobot_isi_a':isi_arr_a,'bobot_isi_b':isi_arr_b,'bobot_isi_c':isi_arr_c,
                                                  'bobot_pao_a':pao_arr_a,'bobot_pao_b':pao_arr_b,'bobot_pao_c':pao_arr_c,
						  'bobot_time_a':time_arr_a,'bobot_time_b':time_arr_b,'bobot_time_c':time_arr_c,
				     'bobot_cruelty_free_a':cruelty_free_arr_a,'bobot_cruelty_free_b':cruelty_free_arr_b,'bobot_cruelty_free_c':cruelty_free_arr_c,
                                                  'kri_a':int(kri_a),'kri_b':int(kri_b),'kri_c':int(kri_c),'kri_d':int(kri_d),'kri_e':int(kri_e),'kri_e':int(kri_e),'kri_f':int(kri_f),'kri_g':int(kri_g),'kri_h':int(kri_h),'kri_i':int(kri_i),'kri_j':int(kri_j),
                                                  'bobot_harga':kri_harga,'bobot_isi':kri_isi,'bobot_pao':kri_pao,'bobot_time':kri_time,'bobot_cruelty_free':kri_cruelty_free,

                                                  'produk_a':produk_a,'produk_b':produk_b,'produk_c':produk_c,
                                                  'produk_max':produk[inde],'cons':cons,'cons_pre':cons*100,
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
	kri_g=float(kri[6])
	kri_h=float(kri[7])
	kri_i=float(kri[8])
	kri_j=float(kri[9])
        kri_arr=np.array([1,kri_a,kri_b,kri_c,kri_d,
                          1/kri_a,1,kri_e,kri_f,kri_g,
                          1/kri_b,1/kri_e,1,kri_h,kri_i,
			  1/kri_c,1/kri_f,1/kri_h,1,kri_j,
                          1/kri_d,1/kri_g,1/kri_i,1/kri_j,1])
        kri_arr=kri_arr.reshape(5,5)
        cons=calculateConsistency(kri_arr)

	kri_arr=calculateWeights(kri_arr)
	kri_harga=kri_arr[0]
        kri_isi=kri_arr[1]
        kri_pao=kri_arr[2]
        kri_time=kri_arr[3]
	kri_cruelty_free=kri_arr[4]

        kri_arr=np.array(kri_arr)
        kri_arr=kri_arr.reshape(5,1)

        return render(request,self.template_name,{'kri_a':int(kri_a),'kri_b':int(kri_b),'kri_c':int(kri_c),'kri_d':int(kri_d),'kri_e':int(kri_e),'kri_e':int(kri_e),'kri_f':int(kri_f),'kri_g':int(kri_g),'kri_h':int(kri_h),'kri_i':int(kri_i),'kri_j':int(kri_j),
                                                  'bobot_harga':kri_harga,'bobot_isi':kri_isi,'bobot_pao':kri_pao,'bobot_time':kri_time,'bobot_cruelty_free':kri_cruelty_free,

                                                  'cons':cons,'cons_pre':cons*100,'alternatif':alternatif
                                                    
                                                    })

class InputNamaView(View):
    template_name = 'ahp/input-nama.html'
    id = None
    def get(self, request, id):
        ahp = Alternatif.objects.get(id=id)
        form = NamaProdukForm(instance=ahp)
        return render(request,self.template_name,{'form':form,'ahp':ahp})

    def post(self, request, id=None):
        ahp_ob = Alternatif.objects.get(id=id)
        form = NamaProdukForm(request.POST, instance=ahp_ob)
        if form.is_valid():
            ahp=form.save(commit=False)
            produk_a=form.cleaned_data['produk_a']
            produk_b=form.cleaned_data['produk_b']
            produk_c=form.cleaned_data['produk_c']
            produk=[]
            produk.append(produk_a),produk.append(produk_b),produk.append(produk_c)
            ahp.nama_product= json.dumps(produk)
            ahp.save()
            messages.success(request,'Input nama produk telah berhasil')
            return HttpResponseRedirect(reverse('input-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'Ada kesalahan saaat input nama produk, mohon ulangi lagi')
            return render(request,self.template_name,{'form':form})
