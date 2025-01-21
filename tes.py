def cetak_nota(items):
    print("\n=====================")
    print("       NOTA KASIR    ")
    print("=====================")
    total = 0
    for item in items:
        nama, harga, jumlah = item
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nama} - {harga} x {jumlah} = {subtotal}")
    
    print("=====================")
    print(f"Total: {total}")
    print("=====================")

def main():
    items = []
    while True:
        nama = input("Masukkan nama barang (atau ketik 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break
        harga = float(input("Masukkan harga barang: "))
        jumlah = int(input("Masukkan jumlah barang: "))
        items.append((nama, harga, jumlah))
    
    cetak_nota(items)

if __name__ == "__main__":
    main()