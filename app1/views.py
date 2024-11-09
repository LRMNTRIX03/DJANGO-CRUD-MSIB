from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormBarang
from django.contrib import messages
from .models import Barang


def inputBarang_view(request):
    form = FormBarang()
    if request.method == 'POST':
        form = FormBarang(request.POST)
        if form.is_valid():
            if Barang.objects.filter(nama_barang=form.cleaned_data['nama_barang']).exists():
                messages.error(request, 'Barang Sudah Ada')
            else:
                Barang.objects.create(
                    nama_barang=form.cleaned_data['nama_barang'],
                    harga=form.cleaned_data['harga_barang'],
                    stok=form.cleaned_data['stok_barang'],
                    keterangan=form.cleaned_data['keterangan_barang']
                )
                messages.success(request, 'Berhasil Memasukan barang')
                return redirect('app1:inputbarang')
        else:
            messages.error(request, 'Gagal Memasukan barang')
    return render(request, 'app1/input_barang.html', {'form': form, 'title': 'Input Barang'})


def tampilBarang_view(request):
    context = {
        'title': 'Tampil Barang',
        'barang': Barang.objects.all()
    }
    return render(request, 'app1/output_barang.html', context)


def editBarang_view(request, id):
    barang = get_object_or_404(Barang, id=id)
    form = FormBarang(request.POST or None, initial={
        'nama_barang': barang.nama_barang,
        'harga_barang': barang.harga,
        'stok_barang': barang.stok,
        'keterangan_barang': barang.keterangan
    })

    if request.method == 'POST' and form.is_valid():
        barang.nama_barang = form.cleaned_data['nama_barang']
        barang.harga = form.cleaned_data['harga_barang']
        barang.stok = form.cleaned_data['stok_barang']
        barang.keterangan = form.cleaned_data['keterangan_barang']
        barang.save()
        messages.success(request, 'Barang berhasil diperbarui')
        return redirect('app1:showbarang')

    context = {
        'title': 'Edit Barang',
        'form': form,
        'barang': barang
    }
    return render(request, 'app1/update_barang.html', context)

# View for deleting a specific Barang item
def DeleteBarang_view(request, id):
    barang = get_object_or_404(Barang, id=id)
    barang.delete()
    messages.success(request, 'Barang berhasil dihapus')
    return redirect('app1:showbarang')
