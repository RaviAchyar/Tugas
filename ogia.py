
kwh = int(input("masukkan penggunaan: "))

Kipas = int(input("masukkan watt kipas: "))
Lampu = int(input("masukkan watt lampu: "))
Tv = int(input("masukkan watt tv: "))

Kipas = Kipas * kwh

print("kipas * penggunaan:", Kipas)
print("lampu * pengunaan:", Lampu)
print("tv * pengunaan:", Tv)

total_watt = hitung_total_watt (Kipas, Lampu, Tv)

input(f"panjang sisi miring (c) adalah:{sisi_miring:.2f}")