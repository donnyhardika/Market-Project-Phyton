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
        print(
            f"Jumlah yang dimasukkan terlalu banyak. Stock apel tinggal: {stock_apel}"
        )

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
