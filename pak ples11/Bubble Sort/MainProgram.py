# File utama: main.py
import ClassBubble  # pastikan ClassBubble.py ada di direktori yang sama

def GenerateElement():
    dataelement = [39, 12, 18, 85, 72, 10, 2, 18, 44, 56]
    return dataelement

def MainMenu():
    element = GenerateElement()
    print("Data array sebelum sorting: ", element)
    pilih = "y"
    while pilih.lower() == "y":
        print("| Menu Aplikasi Sorting Data |")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("==============================")

        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            hasil = SortingBubble.ProsesBubble(element.copy())
            print("Data array setelah sorting menggunakan Bubble Sort: ", hasil)
        else:
            print("Menu sorting belum lengkap ...")

if __name__ == "__main__":
    SortingBubble = ClassBubble.BubbleSorting()
    MainMenu()
