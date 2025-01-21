def input_belanja():
    belanja = []
    belanja = ['nama'] = input("Masukkkan nama barang : ")
    belanja = ['jumlah'] = int(input("Masukkan jumlah: "))
    belanja= ['harga'] = float(input("Masukkan harga : "))
    return belanja

def hitung_total(keranjang):
    total = 0
    for barang in keranjang:
        total += barang['jumlah'] * barang['harga']
        return total

def tambah_belanja(keranjang):
    keranjang.append(input_belanja())
    return keranjang

if __name__ == "__main__":
    keranjang = []
    lanjut = 'y'
    while(lanjut == 'y'):
        keranjang = tambah_belanja(keranjang)
        print("{:^10} | {:^25} | {:^23} ".format('nama', 'jumlah', 'harga'))
        print('-------------------------------------------------------------------------------------')
        for belanja in keranjang:
            print("{:^10} | {:^25} | {:^23} ".format(belanja['nim'], belanja['nama'], belanja['prodi']))
        lanjut = input("Tambah belanja (y/t) ?")
        total = hitung_total(keranjang)
        print(f"/ntotal belanja :", 'Rp.', total)
            
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