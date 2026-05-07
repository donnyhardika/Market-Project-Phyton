print("=== PROGRAM BELANJA BUAH ===\n")
# Nama: Donny Aditya Hardika

# Tentukan stock awal
stock_apel = 10
stock_jeruk = 7
stock_anggur = 6

# Harga buah
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

# Input jumlah apel dengan validasi stock
while True:
    jumlah_apel = int(input("Masukkan jumlah apel: "))
    if jumlah_apel <= stock_apel:
        break
    else:
        print(f"Jumlah yang dimasukkan terlalu banyak. Stock apel tinggal: {stock_apel}")

print(f"Jumlah apel yang dibeli: {jumlah_apel}")
print(f"Total harga apel: Rp {jumlah_apel * harga_apel:,}")


# Input jumlah jeruk dengan validasi stock
while True:
    jumlah_jeruk = int(input("Masukkan jumlah jeruk: "))
    if jumlah_jeruk <= stock_jeruk:
        break
    else:
        print(
            f"Jumlah yang dimasukkan terlalu banyak. Stock jeruk tinggal: {stock_jeruk}"
        )

# Input jumlah anggur dengan validasi stock
while True:
    jumlah_anggur = int(input("Masukkan jumlah anggur: "))
    if jumlah_anggur <= stock_anggur:
        break
    else:
        print(
            f"Jumlah yang dimasukkan terlalu banyak. Stock anggur tinggal: {stock_anggur}"
        )

# Hitung total belanja
total_apel = jumlah_apel * harga_apel
total_jeruk = jumlah_jeruk * harga_jeruk
total_anggur = jumlah_anggur * harga_anggur
total = total_apel + total_jeruk + total_anggur

# Cetak detail belanja
print("\n=== Detail Belanja ===")
print("Apel  :", jumlah_apel, "x", harga_apel, "=", total_apel)
print("Jeruk :", jumlah_jeruk, "x", harga_jeruk, "=", total_jeruk)
print("Anggur:", jumlah_anggur, "x", harga_anggur, "=", total_anggur)
print("Total :", total)

# Proses pembayaran dengan validasi
while True:
    uang = int(input("\nMasukkan jumlah uang: "))
    if uang < total:
        kurang = total - uang
        print(f"Uang anda kurang sebesar Rp {kurang:,}. Silakan masukkan lagi.")
    elif uang == total:
        print("Terima kasih")
        break
    else:
        kembalian = uang - total
        print("Terima kasih")
        print(f"Uang kembali anda: Rp {kembalian:,}")
        break


print("=== PROGRAM MARKET BUAH ===\n")

# Daftar buah awal (list of dict)
buah_list = [
    {"nama": "Apel", "harga": 10000, "stock": 10},
    {"nama": "Jeruk", "harga": 15000, "stock": 7},
    {"nama": "Anggur", "harga": 20000, "stock": 6},
]

# Keranjang belanja
cart = []

# Fungsi menampilkan daftar buah
def tampilkan_buah():
    print("\n=== Daftar Buah ===")
    for idx, buah in enumerate(buah_list, start=1):
        print(
            f"{idx}. {buah['nama']} - Harga: Rp {buah['harga']:,} - Stock: {buah['stock']}"
        )

# Fungsi menambah buah
def tambah_buah():
    nama = input("Masukkan nama buah baru: ")
    harga = int(input("Masukkan harga buah: "))
    stock = int(input("Masukkan stock buah: "))
    buah_list.append({"nama": nama, "harga": harga, "stock": stock})
    print(f"{nama} berhasil ditambahkan!")
    tampilkan_buah()

# Fungsi menghapus buah
def hapus_buah():
    tampilkan_buah()
    idx = int(input("Masukkan nomor buah yang ingin dihapus: "))
    if 1 <= idx <= len(buah_list):
        buah = buah_list.pop(idx - 1)
        print(f"{buah['nama']} berhasil dihapus!")
    else:
        print("Nomor buah tidak valid.")
    tampilkan_buah()

# Fungsi membeli buah
def beli_buah():
    tampilkan_buah()
    while True:
        idx = int(input("Masukkan nomor buah yang ingin dibeli (0 untuk selesai): "))
        if idx == 0:
            break
        if 1 <= idx <= len(buah_list):
            jumlah = int(input("Masukkan jumlah: "))
            if jumlah <= buah_list[idx - 1]["stock"]:
                cart.append({"nama": buah_list[idx - 1]["nama"],
                             "harga": buah_list[idx - 1]["harga"],
                             "jumlah": jumlah})
            else:
                print("Stock tidak mencukupi.")
        else:
            print("Nomor buah tidak valid.")

    # Hitung total belanja
    total = sum(item["harga"] * item["jumlah"] for item in cart)
    print("\n=== Detail Belanja ===")
    for item in cart:
        print(f"{item['nama']} : {item['jumlah']} x {item['harga']} = Rp {item['harga']*item['jumlah']:,}")
    print(f"Total : Rp {total:,}")

    # Proses pembayaran
    while True:
        uang = int(input("\nMasukkan jumlah uang: "))
        if uang < total:
            print(f"Uang anda kurang Rp {total - uang:,}. Silakan masukkan lagi.")
        else:
            print("Terima kasih telah berbelanja!")
            if uang > total:
                print(f"Uang kembali anda: Rp {uang - total:,}")
            # Kurangi stock
            for item in cart:
                for buah in buah_list:
                    if buah["nama"] == item["nama"]:
                        buah["stock"] -= item["jumlah"]
            cart.clear()
            break

# Main loop
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Menampilkan daftar buah")
    print("2. Menambah buah")
    print("3. Menghapus buah")
    print("4. Membeli buah")
    print("5. Exit Program")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_buah()
    elif pilihan == "2":
        tambah_buah()
    elif pilihan == "3":
        hapus_buah()
    elif pilihan == "4":
        beli_buah()
    elif pilihan == "5":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid.")

print("=== PROGRAM MARKET BUAH (Dictionary) ===\n")

# Daftar buah awal (dictionary)
buah_dict = {
    "Apel": {"harga": 10000, "stock": 10},
    "Jeruk": {"harga": 15000, "stock": 7},
    "Anggur": {"harga": 20000, "stock": 6},
}

# Keranjang belanja
cart = []

# Fungsi menampilkan daftar buah
def tampilkan_buah():
    print("\n=== Daftar Buah ===")
    for idx, (nama, info) in enumerate(buah_dict.items(), start=1):
        print(f"{idx}. {nama} - Harga: Rp {info['harga']:,} - Stock: {info['stock']}")

# Fungsi menambah buah
def tambah_buah():
    nama = input("Masukkan nama buah baru: ")
    harga = int(input("Masukkan harga buah: "))
    stock = int(input("Masukkan stock buah: "))
    buah_dict[nama] = {"harga": harga, "stock": stock}
    print(f"{nama} berhasil ditambahkan!")
    tampilkan_buah()

# Fungsi menghapus buah
def hapus_buah():
    tampilkan_buah()
    nama = input("Masukkan nama buah yang ingin dihapus: ")
    if nama in buah_dict:
        del buah_dict[nama]
        print(f"{nama} berhasil dihapus!")
    else:
        print("Nama buah tidak ditemukan.")
    tampilkan_buah()

# Fungsi membeli buah
def beli_buah():
    tampilkan_buah()
    while True:
        nama = input("Masukkan nama buah yang ingin dibeli (ENTER untuk selesai): ")
        if nama == "":
            break
        if nama in buah_dict:
            jumlah = int(input("Masukkan jumlah: "))
            if jumlah <= buah_dict[nama]["stock"]:
                cart.append({"nama": nama,
                             "harga": buah_dict[nama]["harga"],
                             "jumlah": jumlah})
            else:
                print("Stock tidak mencukupi.")
        else:
            print("Nama buah tidak valid.")

    # Hitung total belanja
    total = sum(item["harga"] * item["jumlah"] for item in cart)
    print("\n=== Detail Belanja ===")
    for item in cart:
        print(f"{item['nama']} : {item['jumlah']} x {item['harga']} = Rp {item['harga']*item['jumlah']:,}")
    print(f"Total : Rp {total:,}")

    # Proses pembayaran
    while True:
        uang = int(input("\nMasukkan jumlah uang: "))
        if uang < total:
            print(f"Uang anda kurang Rp {total - uang:,}. Silakan masukkan lagi.")
        else:
            print("Terima kasih telah berbelanja!")
            if uang > total:
                print(f"Uang kembali anda: Rp {uang - total:,}")
            # Kurangi stock
            for item in cart:
                buah_dict[item["nama"]]["stock"] -= item["jumlah"]
            cart.clear()
            break

# Main loop
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Menampilkan daftar buah")
    print("2. Menambah buah")
    print("3. Menghapus buah")
    print("4. Membeli buah")
    print("5. Exit Program")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_buah()
    elif pilihan == "2":
        tambah_buah()
    elif pilihan == "3":
        hapus_buah()
    elif pilihan == "4":
        beli_buah()
    elif pilihan == "5":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid.")
