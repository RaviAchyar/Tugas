databarang = []

def format_currency(value):
    return f"Rp{value:,.2f}"

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

def cetak_transaksi(databarang):
    print("\n+====================== Anjay Store ======================+")
    print()
    print("{:<10} | {:^8} | {:<15} |  {:<14} |".format('Nama', 'Jumlah', 'Harga' ,'Subtotal'))
    print("+---------------------------------------------------------+")
    
    total = 0
    for barang in databarang:
        nama_barang = barang["nama barang"]
        harga_barang = barang["harga barang"]
        jumlah_barang = barang["jumlah barang"]
        sub = barang["SubTotal"]
        total += sub
        print("{:<10} | {:^8} | {:<15} |  {:<14} |".format(nama_barang, jumlah_barang, format_currency(harga_barang), format_currency(sub)))
        
    print("+=========================================================+")
    print()
    print(f"{'Total:' :<30}{format_currency(total).rjust(14)}")
    print()
    
    return total

def pembayaran(subtotal):
    while True:
        try:
            # Diskon
            diskon = 0
            if subtotal >= 50000:
                diskon = subtotal * 0.10  # Diskon 10%
            total_setelah_diskon = subtotal - diskon
            
            print(f"{'Total setelah diskon:' :<30}{format_currency(total_setelah_diskon).rjust(14)}")
            print()
            print("-----------------------------------------------------------")
            
            # Input jumlah uang dari pengguna
            pembayaran_amount = input(f"{'Jumlah uang: Rp' :<30}")
            
            # Validasi input untuk memastikan itu adalah angka
            if not pembayaran_amount.isdigit():
                print("Input tidak valid! Pastikan untuk memasukkan angka yang benar.")
                continue
            
            pembayaran_amount = int(pembayaran_amount)
            
            if pembayaran_amount < total_setelah_diskon:
                print("Jumlah pembayaran kurang dari total yang harus dibayar! Silakan masukkan jumlah yang cukup.")
            else:
                kembalian = pembayaran_amount - total_setelah_diskon
                print()
                print(f"{'Kembalian:' :<30}{format_currency(kembalian).rjust(14)}")
                return pembayaran_amount, kembalian
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
            total = cetak_transaksi(databarang)  # Print the transaction details
            pembayaran(total)
            print()
            print("====================== Terima kasih ======================")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih sesuai nomor.")

menu()