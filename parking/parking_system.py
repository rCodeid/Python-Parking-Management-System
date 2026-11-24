print("======= SISTEM PARKIR=======")
import datetime
sudah_masuk = False
while True:

    print("1. masuk")
    print("2. keluar")

    menu=(input("pilih menu (nomor) : "))

    if menu == "1":

        jenis_kendaraan=input("jenis kendaraan (motor/mobil) : ")

        if jenis_kendaraan != "motor" and jenis_kendaraan != "mobil":
            print("kendaraan tidak tersedia")
            continue
        waktu_masuk= datetime.datetime.now()
        sudah_masuk = True

        print("===== TIKET PARKIR =====")
        print(f"{'kendaraan':15} : {jenis_kendaraan}")
        print(f"{'masuk':15} : {waktu_masuk.strftime('%H:%M')}")
       
    elif menu == "2":

        if sudah_masuk == False:
         print("Kendaraan belum masuk!")
         continue
        waktu_keluar= datetime.datetime.now()
        lama_parkir = waktu_keluar - waktu_masuk
        total_jam= lama_parkir.total_seconds() / 3600

        jam_bayar = int(total_jam)

        if total_jam > jam_bayar:
          jam_bayar +=1
                
        if jenis_kendaraan == "motor":
            harga= jam_bayar * 2000
            print("Kendaraan diterima")

        elif jenis_kendaraan == "mobil":
            harga= jam_bayar * 5000
            print("Kendaraan diterima")


        if jam_bayar >4:
         diskon = harga* 10 / 100
          
        else:
         diskon= 0
          
        total_bayar = harga - diskon
           
        print("===== TIKET PARKIR =====")
        print(f"{'kendaraan':15} : {jenis_kendaraan}")
        print(f"{'keluar':15} : {waktu_keluar.strftime('%H:%M')}")
        print(f"{'lama parkir':15} : {str(lama_parkir).split('.')[0]}")
        print(f"{'harga':15} : Rp{harga:,.0f}".replace(",", "."))
        print(f"{'diskon':15} : {diskon}")
        print(f"{'total bayar':15} : Rp{total_bayar:,.0f}".replace(",", "."))
        sudah_masuk = False