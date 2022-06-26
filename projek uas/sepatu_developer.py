import os
import time
import pandas as pd

t = 60
def cooldown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = 'Coba lagi dalam {:02d}:{:02d}'.format(mins, secs).center(60)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def hapusLayar(): 
    os.system('cls')

def garis():
    print(60*'-')

def equals():
    print(60*'=')

def buka():
    print('')
    print('..::SELAMAT DATANG DI GROBAK SEPATU VANS::..'.center(60))

def toko():
    print('GROBAK SEPATU VANS'.center(60))
    print('Jl. Seksama no.20'.center(60))
    print('Kota Spacetoon Future'.center(60))
    print('No. Telp (021) 210 012 20 '.center(60))

def menu():
    print('Kode\t\t     Jenis Sepatu\t\tHarga')
    garis()
    print('ATH\t\t     Authentic\t\t\tRp 600.000')
    print('BDN\t\t     Bold Ni\t\t\tRp 1.049.000')
    print('BSN\t\t     Bess Ni\t\t\tRp 959.200')
    print('CTY\t\t     City Trl\t\t\tRp 1.439.000')
    print('DCS\t\t     Decon Sf\t\t\tRp 1.099.000')
    print('ERA\t\t     Era Pro\t\t\tRp 750.000')
    print('OLD\t\t     Old Skool\t\t\tRp 800.000')
    print('SKL\t\t     Sk8 Low\t\t\tRp 1.199.000')
    print('SKM\t\t     Sk8 Mid\t\t\tRp 1.079.100')
    print('SKH\t\t     Sk8 High\t\t\tRp 1.399.000')
    print('SPT\t\t     Sport\t\t\tRp 999.000')
    print('STL\t\t     Style 36\t\t\tRp 1.099.000')

## membuat global variable
edile = 1 
## jika ingin tahu tentang global variables dll kunjungi https://www.w3schools.com/python/python_variables_global.asp

## Log-in sebelum start untuk menjaga keamanan
## Karena jika username atau password salah akan cooldown dalam 1 menit
def login(): 
    salah = 1
    while salah <= 3:
        print('')
        username = str(input("Username : "))
        password = str(input("Password : "))
        t = 60

        salah += 1

        if username == 'admin' or username == 'ADMIN':
            if password == '1234':
                start()
            else:
                print("Username atau Password Salah")
        else:
            if password == '1234':
                print("Username atau Password Salah")
            else:
                print("Username atau Password Salah")
        if salah > 3:
            print('')
            cooldown(int(t))
            hapusLayar()
            buka()
            login()

def start(): ## memulai program
    hapusLayar() # Function untuk menghapus layar agar output rapih
    equals()
    toko()
    equals()

    # mengambil waktu dan tanggal sekarang
    waktu = time.localtime() 
    tanggal = time.strftime("%a %D %H:%M:%S", waktu)
    print(f'{tanggal}','Kasir : ADMIN'.rjust(38))

    garis()
    menu()
    garis()
    print('''Note : - Tidak ada ukuran 1-30 dan 56-100
       - DISKON 30% jika beli 3 sepatu!''')
    garis()

    ## membuat variabel / list
    kode = []
    nama_barang = []
    harga = []
    jumlah_beli = []
    jumlah_harga = []
    ukuran = []

    print('')
    p = int(input('Ingin berapa jenis sepatu\t: '))

    ## Melakukan perulangan for
    for i in range(p):
        print(f'Data {i+1}')
        kode.append(input('Input kode sepatu\t\t: '))
        ukuran.append(int(input('Input ukuran sepatu\t\t: ')))
        jumlah_beli.append(int(input('Input jumlah pembelian\t\t: ')))
        
        if kode[i] == "ATH" or kode[i] == "ath":
            nama_barang.append('Authentic')
            harga.append(600000)
        elif kode[i] == "BDN" or kode[i] == 'bdn':
            nama_barang.append('Bold Ni')
            harga.append(1049000)
        elif kode[i] == "BSN" or kode[i] == 'bsn':
            nama_barang.append('Bess Ni')
            harga.append(959200)
        elif kode[i] == "CTY" or kode[i] == 'cty':
            nama_barang.append('City Trl')
            harga.append(1439000)
        elif kode[i] == "ERA" or kode[i] == 'era':
            nama_barang.append('Era Pro')
            harga.append(750000)
        elif kode[i] == "DCS" or kode[i] == 'dcs':
            nama_barang.append('Decon Sf')
            harga.append(1099000)
        elif kode[i] == "OLD" or kode[i] == 'old':
            nama_barang.append('Old Skool')
            harga.append(800000)
        elif kode[i] == "SKL" or kode[i] == 'skl':
            nama_barang.append('Sk8 Low')
            harga.append(1199000)
        elif kode[i] == "SKH" or kode[i] == 'skh':
            nama_barang.append('Sk8 High')
            harga.append(1399000)
        elif kode[i] == "SKM" or kode[i] == 'skm':
            nama_barang.append('Sk8 Mid')
            harga.append(1079100)
        elif kode[i] == "SPT" or kode[i] == 'spt':
            nama_barang.append('Sport')
            harga.append(999000)
        elif kode[i] == "STL" or kode[i] == 'stl':
            nama_barang.append('Style 36')
            harga.append(1099000)
        else:
            print('\n')
            print("Kode yang anda masukkan salah!".center(60))
            print('Silahkan login kembali.'.center(60))
            kembaliKeMenu()
            
        ## percabangan if untuk note
        if ukuran[i] <= 30 or ukuran[i] >= 56 :
            t = 3
            print('>> Ukuran untuk ukuran 1-30 dan 56-100 TIDAK ADA! <<')       
            print('Kembali ke menu awal dalam ',cooldown(int(t)))
            start()

    ## rumus menghitung pembelian
    for i in range(p):
        jumlah_harga.append(harga[i] * jumlah_beli[i])

    ## menjumlahkan setiap harga yg ada dalam jumlah_harga menggunakan modul sum()
    total_harga = sum(jumlah_harga) 
    pajak = total_harga * 0.1 
    total_bayar = total_harga + pajak

    # membuat data yang akan diformat ke pandas
    data = {
        'Jenis Sepatu' : nama_barang,
        'UK Sepatu' : ukuran,
        'Harga' : harga,
        'Jumlah Item' : jumlah_beli,
        'Jumlah Harga' : jumlah_harga
    }

    struk = pd.DataFrame(data) # memformat data dengan pandas

    hapusLayar() # Function untuk menghapus layar agar output rapih
    time.sleep(0.5)
    equals()
    toko()
    equals()

    # mengambil waktu dan tanggal sekarang
    waktu = time.localtime() 
    tanggal = time.strftime("%a %D %H:%M:%S", waktu)
    print(f'{tanggal}','Kasir : ADMIN'.rjust(38))
    
    garis()

    print(struk)  ## memanggil kembali output data yang tadi di format
    
    garis()

    # mencetak hasil perhitungan pembelian
    print(f'Total Item         : {sum(jumlah_beli)}')
    print(f'Jumlah Bayar       : Rp.{total_harga}')
    print(f'Pajak 10%          : Rp.{pajak}')
    garis()

    if sum(jumlah_beli) >= 3: ## Menghitung jumlah diskon
        diskon = total_harga * 0.3
        total_bayar = total_bayar - diskon
        print(f'**Diskon 30%       : Rp.{diskon}')
        garis()
    print(f'Total Bayar        : Rp.{total_bayar}')
    bayar = int(input('Pembayaran Tunai   : Rp.')) ## Input pembayaran

    ## Perulangan jika uangnya kurang sampai uangnya cukup
    while bayar < total_bayar:

        print('\nUang anda kurang !')
        kurang = input('\nIngin membayar [Y/N] : ')
        if kurang == 'Y' or kurang == 'y':
            bayar = int(input('\nPembayaran Tunai   : Rp.'))
            
        elif kurang == 'N' or kurang == 'n':
            print('')
            print('XXXX PEMBAYARAN GAGAL XXXX'.center(60))
            kembaliKeMenu()
            quit() 
        else:
            print('Kode yang anda masukkan salah !')
            if bayar >= total_bayar:
                break

    ## Menghitung kembalian
    k = bayar - total_bayar
    print(f'Kembalian          : Rp.{k}')

    ## Tampilan penutup program
    garis()
    akhir()
    equals()
    print('')
    kembaliKeMenu() ## memanggil function kembali ke menu

def kembaliKeMenu(): ## function untuk kembali ke menu start

    print("")
    kembali = input("Ingin kembali ke menu [Y/N] : ")
    if kembali == 'Y' or kembali == 'y' :
        start()
    elif kembali == 'N' or kembali == 'n':
        hapusLayar()
        quit()


def akhir():
    print('..::Terimakasih Atas Kunjungan Anda::..'.center(60))
    print('..::Silahkan Datang Kembali::..'.center(60))


