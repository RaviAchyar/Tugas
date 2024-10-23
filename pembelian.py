#kamus
harga = 0
qty = 0
total_harga = 0
bayar = 0
kembalian = 0

#algoritma
harga = int(input("input harga barang : "))
qty = int(input("input jumlah barang : "))
total_harga = harga * qty
print("total harga = ", total_harga)
pembayaran = int(input("input pembayaran barang : "))
kembalian = pembayaran - total_harga
print("kembalian =", kembalian)