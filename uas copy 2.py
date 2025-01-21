def tampil_keranjang(keranjang):
    for barang in keranjang:
        print(f"| {barang['nama']} | jumlah: {barang['jumlah']} | harga: {barang['harga']}|")

def hitung_total(keranjang):
    total = 0
    for barang in keranjang:
        total += barang['jumlah'] * barang['harga']
        return total
    
def main():
    keranjang = []
    while True:
        pilihan = input("Masukkan Barang? (y/t):")
        
        if pilihan == 'y':
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah: "))
            harga = float(input("masukkan harga: " ))
            
            keranjang.append({'nama' : nama_barang,'jumlah' : jumlah, 'harga' : harga})
            print(f"{nama_barang} telah ditambahkan ke keranjang")
            
        elif pilihan == 't' :
            total = hitung_total(keranjang)
            print(f"total belanja :", 'Rp.', total)
            
            if (total >= 50000):
                diskon = total * 0.10
            else:
                diskon = 0
            total_setelah_diskon = total - diskon
            print("total setelah diskon:", 'Rp.', total_setelah_diskon)           
            uang = float(input("masukkan jumlah uang: "))
            kembalian = uang - total_setelah_diskon
            
            print("======================= YteamMart ======================")
            print("{:^10} | {:^10} | {:^23} |".format('nama', 'jumlah', 'harga'))
            print("--------------------------------------------------------")
            print("{:^10} | {:^10} | {:^23} |".format(nama_barang, jumlah, harga))  
            print("Uang :", uang)
            print("kembalian :", 'Rp.', kembalian)
            print("===================== terima kasih =====================")
            break
        
        else:
            print("pilihan tidak valid, pilih 1, 2, atau 3.")

main()