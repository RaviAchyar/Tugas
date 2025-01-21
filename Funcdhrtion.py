def hitung_penggunaan_listrik(daya, waktu):
    """
    Menghitung penggunaan energi listrik dalam kWh.
    daya (watt) : daya alat listrik
    waktu (jam) : waktu penggunaan
    """
    # Mengubah daya dari watt ke kWh (1 kW = 1000 watt)
    daya_kWh = daya / 1000
    # Menghitung penggunaan energi
    energi = daya_kWh * waktu
    return energi

def hitung_biaya_listrik(energi, tarif):
    """
    Menghitung biaya listrik berdasarkan penggunaan energi.
    energi (kWh) : jumlah energi yang digunakan
    tarif (Rp/kWh) : tarif listrik per kWh
    """
    biaya = energi * tarif
    return biaya

# Contoh penggunaan
daya_ac = 1000  # daya AC dalam watt
waktu_penggunaan = 5  # waktu penggunaan dalam jam
tarif_listrik = 1500  # tarif listrik per kWh dalam Rupiah

# Menghitung penggunaan energi
energi = hitung_penggunaan_listrik(daya_ac, waktu_penggunaan)
# Menghitung biaya
biaya = hitung_biaya_listrik(energi, tarif_listrik)

print(f"Penggunaan energi: {energi} kWh")
print(f"Biaya listrik: Rp {biaya}")
