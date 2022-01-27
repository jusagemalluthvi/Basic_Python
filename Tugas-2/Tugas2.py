#Ini assignment ke-2

print("Selamat datang!")
print("--- Menu ---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
print("=============================================================")

daftar_kontak = {
    "Nama":["Fawwaz","John"],
    "Telepon" : ["08123456789","08987654321"]
}

def masukan ():
    menu = input("Pilih menu : ")
    if menu == "1":
        tampilkan_kontak()
    elif menu == "2":
        tambahkan_kontak()
    elif menu == "3":
        quit()
    else:
        print("Menu tidak tersedia")
    menu2()


def tampilkan_kontak():
    print("=============================================================")
    print("Daftar kontak :")
    for x in daftar_kontak["Nama"]:
        print("Nama : ", x)
        for y in daftar_kontak["Telepon"]:
            if daftar_kontak["Nama"].index(x) == daftar_kontak["Telepon"].index(y):
                print("No Telepon : ", y)
    print("=============================================================")
    menu2()
    masukan()

def tambahkan_kontak():
    print("=============================================================")
    a = input("Tambahkan Nama : ")
    b = input("Tambahkan Nomor Telepon : ")
    daftar_kontak["Nama"].append(a)
    daftar_kontak["Telepon"].append(b)
    print("Kontak berhasil ditambahkan!")
    print("=============================================================")
    menu2()

def menu2():
    print("1. Tampilkan Daftar Kontak")
    print("2. Tambah Kontak (Lagi)")
    print("3. Keluar")
    print("=============================================================")
    masukan()

masukan()


