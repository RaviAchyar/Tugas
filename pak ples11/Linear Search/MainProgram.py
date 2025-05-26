import ClassLinear
def GenerateElement():
    return [39, 12, 18, 85, 72, 10, 2, 18, 44, 56]

def MainMenu():
    element = GenerateElement()
    print("Data array: ", element)
    pilih = "y"
    while pilih == "y":
        print("| Menu Aplikasi Searching Data |")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Recursive Binary Search")
        print("===============================")

        pilihan = int(input("Masukkan Pilihan: "))
        cariData = int(input("Masukkan data yang diinginkan: "))
        if pilihan == "1":
            Linear = SearchLinear.ProsesLinear(element, cariData)
            if (Linear != -1):
                print("Data", cariData, "ditemukan pada indeks ke-", Linear)
            else:
                print("Data tidak ditemukan.")
        else:
            print("Menu sorting belum lengkap ...")

if __name__ == "__main__":
    searcher = ClassLinear.LinearSearching()
    MainMenu()
