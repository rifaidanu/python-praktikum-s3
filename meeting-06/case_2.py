daftar_harga = []

while True:
    nama_barang = input("masukan nama barang, ketik 'selesai' jika sudah: ").lower()
    if nama_barang == "selesai":
        break
    
    harga_barang = int(input("masukan harga barang: "))

    daftar_harga.append(harga_barang)

total_harga = sum(daftar_harga)

harga_diskon = 0
diskon = 0.1

if total_harga > 500000:
    harga_diskon = total_harga * diskon

print(f"Total: {total_harga}")
print("10%" if total_harga > 500000 else "0%")
print(f"Total: {int(total_harga - harga_diskon)}")
