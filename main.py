import method

mtd = method.metod
mtd.identitas(26)

def pesan():
    jmlh = int(input("Jumlah Tiket : "))
    print ("Masukan nama Penumpang")
    for i in range (int(jmlh)):
        i += 1
        n = input("Penumpang ke-{} : ".format(i))
    tot = jmlh*harga
    print("----------------------------------------------")
    email = input("Masukkan email anda: ")
    print("\n----------------------------------------------")
    print("Anda telah berhasil melakukan pembelian tiket ")
    print("E-ticket akan dikirimkan ke email:",email)
    print("----------------------------------------------")
    print("Total Harga","Rp.",(tot))

print("\n===============================")
print("Program Pemesanan Tiket Pesawat")
print("===============================")
print("1. Semarang-Bandung")
print("2. Semarang-Jakarta")
print("3. Semarang-Surabaya")
print("===============================")
tujuan = int(input("Masukan Pilihan [1-3] : "))
    
if ((tujuan) == 1):
    print("\n-------------------------------------------------------")
    print("\t\t Semarang--Bandung")
    print("\nKode  Nama\tWaktu\t\tHarga")
    print("\n      Pesawat\tKeberangkatan\tTiket")
    print("\n-------------------------------------------------------")
    print("\n101.  Garuda\t 08.05 WIB \tRp.1.500.000")
    print("\n102.  Lion Air\t 14.25 WIB \tRp.800.000")
    print("\n103.  Sriwijaya\t 20.45 WIB \tRp.750.000")
    print("\n-------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan : "))
    if ((no_pesawat) == 101):
        harga = 1500000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    elif ((no_pesawat) == 102):
        harga = 800000
        print("")
        print("---------------------------------")
        print("anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    elif ((no_pesawat) == 103):
        harga = 750000
        print("")
        print("---------------------------------")
        print("anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    else :
        print("kode penerbangan tidak ada dalam daftar")
elif ((tujuan) == 2):
    print("\n----------------------------------------------------------")
    print("\t\t Semarang--Jakarta")
    print("\nKode  Nama\tWaktu\t\tHarga")
    print("\n      Pesawat\tKeberangkatan\tTiket")
    print("\n----------------------------------------------------------")
    print("\n201. Citilink\t 09.05 WIB \tRp.2.000.000")
    print("\n202. NAM air\t 15.25 WIB \tRp.900.000")
    print("\n203. Garuda\t 21.45 WIB \tRp.1.200.000")
    print("\n----------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan :"))
    if ((no_pesawat) == 201):
        harga = 2000000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    elif ((no_pesawat) == 202):
        harga = 900000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    elif ((no_pesawat) == 203):
        harga = 1200000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    else :
        print("Kode penerbangan tidak ada dalam daftar")
elif ((tujuan) == 3):
    print("\n-------------------------------------------------------")
    print("\t\t Semarang--Surabaya")
    print("\nKode  Nama\tWaktu\t\tHarga")
    print("\n      Pesawat\tKeberangkatan\tTiket")
    print("\n-------------------------------------------------------")
    print("\n301. Citilink\t 10.05 WIB \tRp.1.000.000")
    print("\n302. Lion Air\t 16.25 WIB \tRp.800.000")
    print("\n303. Garuda\t 22.45 WIB \tRp.1.600.000")
    print("\n-------------------------------------------------------")
    no_pesawat = int(input("Masukan kode penerbangan :"))
    if ((no_pesawat) == 301):
        harga = 1000000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    elif ((no_pesawat) == 302):
        harga = 800000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    elif ((no_pesawat) == 303):
        harga = 1600000
        print("")
        print("---------------------------------")
        print("Anda memilih kode penerbangan",(no_pesawat))
        print("---------------------------------")
        pesan()
    else :
        print("Kode penerbangan tidak ada dalam daftar")
else :
    print("maaf pilihan anda tidak terdaftar")