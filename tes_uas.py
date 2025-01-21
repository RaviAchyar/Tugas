def nota_belanja(keranjang):
    print("\n========== YteamStore ==========")
    total = 0
    for barang in keranjang:
        nama_barang, jumlah, harga = barang
        subtotal = harga * jumlah
        total += subtotal
        print("{:^10} | {:^25} | {:^23} ".format('nama', 'jumlah', 'harga'))
        print("------------------------------------------------------------------")
        print("{:^10} | {:^25} | {:^23} ".format(nama_barang, jumlah, harga,))
        
    print("========================================")
    print(f"Total: {total}")
    print("========================================")
    
def main():
    keranjang = []
    while True:
        nama_barang = input("masukkan nama  barang :")
        if nama_barang.lower() == 't' :
            break
        harga = float(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))
        keranjang.append((nama_barang, harga, jumlah))
        
    nota_belanja(keranjang)

if __name__ == "__main__":    
    main()        