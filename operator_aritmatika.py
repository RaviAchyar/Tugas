#dek
bil1 = 0
bil2 = 0
jumlah = 0
kurang = 0
kali = 0
bagi = 0
hasil_bagi = 0
sisa_bagi = 0
pangkat = 0

#proses
bil1 = int(input("masukkan bilangan 1 : "))
bil2 = int(input("masukkan bilangan 2 : "))

#proses
jumlah = bil1 + bil2
kurang = bil1 - bil2
kali = bil1 * bil2
bagi = bil1 / bil2
hasil_bagi = bil1 // bil2
sisa_bagi = bil1 % bil2
pangkat = bil1 ** bil2

#outpu
print()
print("hasil penjumlahan        : ", jumlah)
print("hasil pengurangan        : ", kurang)
print("hasil perkalian          : ", kali)
print("hasil pembagian          : ", bagi)
print("hasil pembagian genap    : ", hasil_bagi)
print("sisa hasil bagi          : ", sisa_bagi)
print("hasil perpangkatan       : ", pangkat)