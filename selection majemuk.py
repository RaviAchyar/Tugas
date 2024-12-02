nilai= 0
grade = "E"

nilai=int(input("Masukkan nilai:"))
if(nilai >= 90):
    grade= "A"
elif(nilai >= 75):
    grade= "B"
elif(nilai >= 65):
    grade= "C"
elif(nilai >= 55):
    grade= "D"

print(f"Grade Anda = {grade}")