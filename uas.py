def tampil_keranjang(keranjang):
    print("\n================ Keranjang Belanja ===============")
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
        print("\n================= Menu ================")
        print("1. Tambah Barang")
        print("2. Cek Keranjang")
        print("3. Selesai")
        pilihan = input("Pilih menu (1/2/3):")
        
        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah: "))
            harga = float(input("masukkan harga: " ))
            
            keranjang.append({'nama' : nama_barang,'jumlah' : jumlah, 'harga' : harga})
            print(f"{nama_barang} telah ditambahkan ke keranjang")
            
        elif pilihan == '2':
            tampil_keranjang(keranjang)
            
        elif pilihan == '3' :
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
            break
        
        else:
            print("pilihan tidak valid, pilih 1, 2, atau 3.")

main()