import math

def hitung_sisi_miring(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

sisi_a = float(input("masukkan sisi a: "))
sisi_b = float(input("masukkan sisi b: "))

sisi_miring = hitung_sisi_miring (sisi_a, sisi_b)

input(f"panjang sisi miring (c) adalah:{sisi_miring:.2f}")

