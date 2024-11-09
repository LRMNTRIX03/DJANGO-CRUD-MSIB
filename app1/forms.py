from django import forms

class FormBarang(forms.Form):
    nama_barang = forms.CharField(
        label='Nama Barang',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Masukan Nama Barang'})
    )
    harga_barang = forms.IntegerField(
        label='Harga Barang',
        widget=forms.NumberInput(attrs={'class': 'form-control p-3', 'placeholder': 'Masukan Harga Barang'})
    )
    stok_barang = forms.IntegerField(
        label='Stok Barang',
        widget=forms.NumberInput(attrs={'class': 'form-control p-3', 'placeholder': 'Masukan Stok Barang'})
    )
    keterangan_barang = forms.CharField(
        label='Keterangan Barang',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Masukan Keterangan Barang'})
    )
