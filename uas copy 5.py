def nota_belanja(keranjang):
    print("\n================= YteamStore =================")
    print("{:^10} | {:^7} | {:^23} |".format('Nama', 'Jumlah', 'Harga'))
    print("------------------------------------------------")
    
    total = 0
    for barang in keranjang:
        nama_barang, harga, jumlah = barang
        total_barang = harga * jumlah
        total += total_barang
        print("{:^10} | {:^7} | {:^23} |".format(nama_barang, jumlah, harga))
        
    print("================================================")
    print(f"Total: Rp. {total:.2f}")
    
    return total

def main():
    while True:
        keranjang = []
        while True:
            nama_barang = input("Masukkan nama barang: ")
            if nama_barang.lower() == 't':
                break
            else:
                jumlah = int(input("Masukkan jumlah barang: "))
                harga = float(input("Masukkan harga barang: "))
                keranjang.append((nama_barang, harga, jumlah))
        
        if keranjang:  # Cek jika keranjang tidak kosong
            total = nota_belanja(keranjang)
            
            # Hitung diskon
            diskon = 0
            if total >= 50000:
                diskon = total * 0.10  # Diskon 10%
            
            total_setelah_diskon = total - diskon
            print("-------------------------------------------------")
            print(f"Potongan: Rp. {diskon:.2f}")
            print(f"Total setelah diskon: Rp. {total_setelah_diskon:.2f}")
            
            uang = float(input("Jumlah uang: "))
            kembalian = uang - total_setelah_diskon
            print("-------------------------------------------------")
            print(f"Kembalian: Rp. {kembalian:.2f}")
            print("=================================================")
        else:
            print("Keranjang belanja kosong.")
        
        # Tanya pengguna apakah ingin menambah barang
        tambah_barang = input("Tambah barng? (y/t): ")
        if tambah_barang.lower() == 't':
            print("Terima kasih telah berbelanja!")
            break

if __name__ == "__main__":    
    main()