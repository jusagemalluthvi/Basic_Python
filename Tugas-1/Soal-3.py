#Soal nomor 3

Nilai_ujian_teori = float(input("Masukkan nilai ujian teori: "))
Nilai_ujian_praktek = float(input("Masukkan nilai ujian praktek: "))

a = Nilai_ujian_teori
b = Nilai_ujian_praktek

if a >= 70 and b >= 70:
    print("Selamat, anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek.")
elif a < 70 and b >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")