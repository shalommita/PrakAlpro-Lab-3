# SHALOMMITA PRANATANTRI
# 71200640
# INFORMATIKA - UNIVERSITAS KRISTEN DUTA WACANA
# LAB-3-STRUKTUR KONTROL PERCABANGAN

# Membuat nota belanjaan yang sesuai dengan total belanjaan customer
# untuk menentukan apakah cutomer mendapatkan diskon / tidak
print("----------------NOTA BELANJAAN TOKO NGALOR NGIDUL----------------")
print("Jl. Banyu Biru Timur ke Selatan No.115 Sleman, Yogyakarta")
print()
# import datetime : supaya ada data tanggal dan waktu seperti nota pada umumnya
from datetime import datetime
sekarang = datetime.now()
print(sekarang)
print()
# Input
# input nama cutomer (string)
nama = str(input("Masukkan nama Anda:   "))
# input item belanjaan customer (integer)
item = int(input("Item belanjaan Anda (pcs):    "))
# input total belanjaan customer (integer)
total_Belanjaan = int(input("Total belanjaan Anda:  "))

# PORSES : PENGECEKAN 3 KONDISI
# KONDISI 1 ( JIKA TOTAL BELANJAAN >= 500.000 ) : mendapat diskon 20% dan voucher belanja Rp100.000
if total_Belanjaan >= 500000:
    print("Selamat Anda mendapatkan diskon 20%")
    print("dan voucher belanjaan senilai Rp100.000")
    diskon_20 = total_Belanjaan - (total_Belanjaan*20/100)
    print("Total belanjaan akhir Anda sebesari: Rp ", diskon_20)
# KONDISI 2 ( TOTAL BELANJAAN >= 350.000 ) : mendapatkan diskon 10%
elif total_Belanjaan >= 350000:
    print("Selamat Anda mendapatkan diskon 10%")
    diskon_10 = total_Belanjaan - (total_Belanjaan*10/100)
    print("Total belanjaan akhir Anda sebesari : Rp ", diskon_10)
# KONDISI 3 ( TIDAK KEDUANYA ) : tidak mendapatkan diskon / voucher / bonus apapun
else:
    print("Total belanjaan Anda sebesari: Rp ", total_Belanjaan)
    print("Terimakasih sudah berbelanja di toko kami :)")
    
# OUTPUT : Total belanjaan dengan ada/tidaknya diskon