harga_perkwh = 1500  

def hitung_kwh(watt,durasi):
    """fungsi untuk menghitung kwh dari watt dan durasi penggunaan."""
    return watt * durasi / 1000

def hitung_biaya(kwh):
    """fungsi untuk menghitung biaya berdasarkan kwh."""
    return kwh * harga_perkwh

def get_input_penggunaan():
    #input dari pengguna 
    watt_lampu = int(input('masukkan watt lampu ='))
    durasi_lampu = int(input('masukkan durasi penggunaan lampu(jam)= '))
    watt_kipas_angin = int(input('masukkan watt kipas angin = '))
    durasi_kipas_angin = int(input('masukkan durasi penggunaan kipas angin(jam)=  '))
    watt_televisi = int(input('masukkan watt televisi = '))
    durasi_televisi = int(input('masukkan durasi penggunaan televisi = '))

    #proses mencari kwh 
    print()
    kwh_lampu = hitung_kwh(watt_lampu,durasi_lampu)
    kwh_kipas_angin = hitung_kwh(watt_kipas_angin,durasi_kipas_angin)
    kwh_televisi = hitung_kwh(watt_televisi,durasi_televisi)
    total_kwh = kwh_kipas_angin + kwh_lampu + kwh_televisi

    print('kwh lampu = ' , kwh_lampu)
    print('kwh kipas angin = ' , kwh_kipas_angin)
    print('kwh televisi = ' , kwh_televisi)
    print('total kwh = ' , total_kwh, '/kwh')

    #mencari biaya 
    biaya_lampu = hitung_biaya(kwh_lampu)
    biaya_kipas_angin = hitung_biaya(kwh_kipas_angin)
    biaya_televisi = hitung_biaya(kwh_televisi)
    total_biaya = biaya_kipas_angin + biaya_lampu + biaya_televisi

    print('biaya penggunaan lampu selama' , durasi_lampu, 'jam =' , biaya_lampu)
    print('biaya penggunaan kipas angin selama', durasi_kipas_angin, 'jam =' , biaya_kipas_angin)
    print('biaya penggunaan televisi selama' , durasi_televisi, 'jam =' , biaya_televisi)
    print('total biaya ' , total_biaya, '/hari')

    #total per bulan
    total_per_bulan = total_biaya * 30 
    total_kwh_lampu_bulan = kwh_lampu * 30
    total_kwh_kipas_angin_bulan = kwh_kipas_angin * 30
    total_kwh_televisi_bulan = kwh_televisi * 30

    #output per bulan 
    print('total kwh lampu per bulan = ' , total_kwh_lampu_bulan)
    print('total kwh kipas angin = ' , total_kwh_kipas_angin_bulan)
    print('total kwh televisi = ' , total_kwh_televisi_bulan)
    print('total harga per bulan = ' , total_per_bulan)
    
if __name__== "__main__":
    get_input_penggunaan()

    


