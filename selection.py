#variable
pembelian = 0
diskon = 0

pembelian = int(input("Masukkan pembelian: "))
if(pembelian >= 500000):
    diskon = pembelian * 0.05
else:
    diskon = 0

print(f"diskon = {diskon}")