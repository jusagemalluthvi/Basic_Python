#Soal nomor 2

from math import pi

r =  int(input("Masukkan nilai jari-jari lingkaran : "))
π = pi

Luas_lingkaran = float(π * (r**2))
print("\n")

tampilan1 = "Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r,Luas_lingkaran)
print(tampilan1)

#print dengan float 2 angka dibelakang koma
print("\n")
print("Setelah dibulatkan 2 angka dibelakang koma menjadi :")
tampilan2 = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r,Luas_lingkaran)
print(tampilan2)
