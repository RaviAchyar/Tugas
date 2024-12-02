def hitung_biaya_listrik(perangkat):
    """Menghitung total biaya listrik berdasarkan daftar perangkat."""
    total_biaya = 0
    for nama, daya, jam, tarif in perangkat:
        # Menghitung konsumsi energi dalam kWh
        kwh = (daya * jam) / 1000  # daya dalam watt, jadi dibagi 1000 untuk kWh
        biaya = kwh * tarif
        total_biaya += biaya
        print(f"{nama}: {kwh:.2f} kWh, Biaya: {biaya:.2f}")
    return total_biaya

# Daftar perangkat listrik (nama, daya dalam watt, jam penggunaan, tarif per kWh)
perangkat_listrik = [
    ("Kulkas", 150, 24, 1500),  # Kulkas, 150 watt, 24 jam
    ("AC", 2000, 8, 1500),      # AC, 2000 watt, 8 jam
    ("Lampu LED", 10, 5, 1500), # Lampu, 10 watt, 5 jam
    ("TV", 100, 4, 1500)        # TV, 100 watt, 4 jam
]

# Menghitung total biaya listrik
total_biaya = hitung_biaya_listrik(perangkat_listrik)

print(f"\nTotal biaya listrik rumah Anda adalah: {total_biaya:.2f}")

