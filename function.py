def inputan(komentar):
    masukan = int(input(komentar +" ="))
    return masukan


#deklarasi function

def get_total_harga(harga, qty):
    #isi 
    total_harga = harga * qty
    print("total harga",total_harga)
    return total_harga

def get_kembalian(pembayaran, total_harga):
    kembalian = pembayaran - total_harga
    print("kembalian =",kembalian)

def keluaran(nilai):
    print("kembalian =",nilai)

#pemangilan

harga = inputan("harga")
qty = inputan("qty")
total_harga = get_total_harga(harga,qty)
pembayaran = inputan("pembayaran")
get_kembalian(pembayaran, total_harga)

