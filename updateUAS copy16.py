databarang = []

def format_currency(value):
    return f"Rp {value:,.2f}"

def input_barang(databarang):
    while True:
        try:
            nama_barang = input("Nama barang: ")
            jumlah_barang = int(input("Jumlah barang: "))
            harga_barang = int(input("Harga barang: "))
            if jumlah_barang <= 0 or harga_barang <= 0:
                print("Jumlah dan harga harus lebih dari 0.")
                continue
            
            sub = harga_barang * jumlah_barang
            
            # Menambahkan barang yang dimasukkan ke dalam list
            databarang.append({
                "nama barang": nama_barang,
                "jumlah barang": jumlah_barang,
                "harga barang": harga_barang,
                "SubTotal": sub
            })
            print("Barang berhasil dimasukkan")
            break 
        except ValueError:
            print("Input tidak valid! Pastikan untuk memasukkan angka yang benar.")
            
def print_centered(text, width=50): #supaya text center tengah
    print(text.center(width))
    
def cetak_transaksi(databarang):
    print_centered("    ANJAY STORE BANYUWANGI", 50)
    print_centered("    Jl. Jenderal Ahmad Yani No.80, Taman Baru", 50)
    print_centered("    Kec.Banyuwangi, Kabupaten Banyuwangi, Jawa Timur 68416", 50)
    
    print("\n+========================== Kasir ==========================+")
    print("+-----------------------------------------------------------+")
    print("| {:<10} | {:^8} | {:^15} |  {:^14} |".format('Nama', 'Jumlah', 'Harga' ,'Subtotal'))
    print("+-----------------------------------------------------------+")
    
    total = 0
    for barang in databarang:
        nama_barang = barang["nama barang"]
        harga_barang = barang["harga barang"]
        jumlah_barang = barang["jumlah barang"]
        sub = barang["SubTotal"]
        total += sub
        print("| {:<10} | {:^8} | {:<15} |  {:<14} |".format(nama_barang, jumlah_barang, format_currency(harga_barang), format_currency(sub)))
                                                                                          #format_currenc supaya ada 'Rp' dalam nominal              
    print("+===========================================================+")
    print()
    print(f"{'Total:' :<47}{format_currency(total)}")
                            #':>47' atur posisi text >kanan, <kiri 
    
    return total

def pembayaran(subtotal):
    while True:
        try:
            diskon = 0
            if subtotal >= 100000:
                diskon = subtotal * 0.50
            
            total_setelah_diskon = subtotal - diskon
            print(f"{'Total setelah diskon:' :<47}{format_currency(total_setelah_diskon)}")
            
            prompt = f"{'Pembayaran-Tunai:':<20}{'Rp':>29} "
            pembayaran = int(input(prompt))

            if pembayaran < total_setelah_diskon:
                print("Jumlah pembayaran kurang dari total yang harus dibayar! Silakan masukkan jumlah yang cukup.")
            else:
                kembalian = pembayaran - total_setelah_diskon
                print(f"{'Kembalian:' :<47}{format_currency(kembalian)}")
                return pembayaran,kembalian
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.")

def menu(): 
    while True:
        print("-" * 10)
        print("Menu Pilihan")
        print("-" * 10)
        print("1. Tambah barang")
        print("2. Cetak transaksi")
        print("3. Pembayaran")
        pilih = input("Pilih menu (1/2/3): ")
        
        if pilih == "1":
            input_barang(databarang)
        elif pilih == "2":
            cetak_transaksi(databarang)
        elif pilih == "3":
            total = cetak_transaksi(databarang)
            pembayaran(total)
            print()
            print("-----------------------------------------------------------")
            print_centered("Terima Kasih")
            print("==========================================================")
            #text disini supaya bisa muncul jika langsung pilih 3
            break
        else:
            print("Pilihan tidak valid. Silakan pilih sesuai nomor.")

menu()