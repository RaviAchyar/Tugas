# Data penjualan
produk = "Kopi Premium"
harga_satuan = 20000
jumlah_terjual = 150

# Menghitung total penjualan
total_penjualan = harga_satuan * jumlah_terjual

# Menampilkan hasil
print(f"Produk: {produk}")
print(f"Jumlah Terjual: {jumlah_terjual}")
print(f"Harga Satuan:  {harga_satuan}")
print(f"Total Penjualan: {total_penjualan}")
pembayaran = int(input("total penjualan : "))
kembalian = pembayaran - total_penjualan
print("kembalian =", kembalian)