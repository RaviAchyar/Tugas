def hitung_total(keranjang):
    total = 0
    for barang in keranjang:
        total += barang['jumlah'] * barang['harga']
        return total

def barang():
    keranjang = []
    pilihan = 'y'
    nama_barang = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah: "))
    harga = float(input("masukkan harga: " ))
    
    keranjang.append({'nama' : nama_barang,'jumlah' : jumlah, 'harga' : harga})
        
    while (pilihan == 'y'):

        if (pilihan == 't'):
            total = hitung_total(keranjang)
            print("========================")
            print(f"total belanja :", 'Rp.', total)
            
            if (total >= 50000):
                diskon = total * 0.10
            else:
                diskon = 0
                
            total_setelah_diskon = total - diskon
            print("total setelah diskon:", 'Rp.', total_setelah_diskon)
            
            uang = float(input("masukkan jumlah uang: "))
            kembalian = uang - total_setelah_diskon
            print("kembalian :", 'Rp.', kembalian)
            
            print("terima kasih")
            print("============================ YteamMart ===========================")
            print("{:^10} | {:^25} | {:^23} ".format('nama', 'jumlah', 'harga'))
            print("------------------------------------------------------------------")
            print("{:^10} | {:^25} | {:^23} ".format(nama_barang, jumlah, harga))
            pilihan = input("Beli lagi (y/t) ?:")