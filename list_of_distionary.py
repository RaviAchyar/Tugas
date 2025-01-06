def input_mahasiswa():
    mhs = {}
    print("Input Mahasiswa")
    print("---------------")
    mhs['nim'] = input("NIM : ")
    mhs['nama'] = input("Nama : ")
    mhs['prodi'] = input("Prodi : ")
    return mhs


def tambah_mahasiswa(mahasiswa):
    mahasiswa.append(input_mahasiswa())
    return mahasiswa

if __name__ == "__main__":
    mahasiswa = []
    lanjut = 'y'
    while(lanjut == 'y'):
        mahasiswa = tambah_mahasiswa(mahasiswa)
        print("{:^10} | {:<25} | {:^23} ".format('Nim', 'Nama', 'Prodi'))
        print('-------------------------------------------------------------------------------------')
        for mhs in mahasiswa:
            print("{:^10} | {:<25} | {:^23} ".format(mhs['nim'], mhs['nama'], mhs['prodi']))
        lanjut = input("Tambah Mahasiswa (y/t) ?")
        