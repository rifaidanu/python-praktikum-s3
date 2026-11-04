import plistlib
data_barang = [
    {"kode": "BRG001", "nama": "Beras", "harga": 12000, "stok": 50},
    {"kode": "BRG002", "nama": "Gula", "harga": 14000, "stok": 30},
    {"kode": "BRG003", "nama": "Minyak", "harga": 18000, "stok": 20}
]

def add_data(barang, kode_baru, nama_baru, harga_baru: int, stok_baru: int):
    barang.append({"kode":kode_baru, "nama":nama_baru, "harga":harga_baru, "stok":stok_baru})
    show_data(barang)

def show_data(barang):
    print(f"{"NAMA":<8} {"HARGA":<10} {"STOK":<8}")
    print("-"*24)
    for i in data_barang:
        print(f"{i["nama"]:<8} {i["harga"]:<10} {i["stok"]:<8}")

def change_data(barang, kode_target, harga_baru, stok_baru):
    for data in barang:
        if data["kode"] == kode_target:
            data["harga"] = harga_baru
            data["stok"] = stok_baru

    show_data(barang)

def delete_data(barang, kode_target):
    for data in barang:
        if data["kode"] == kode_target:
            data_barang.remove(data)

def transaction(barang):
    keranjang = {}
    while True:
        nama_input = input("Masukkan nama barang (kosongkan/Enter untuk selesai): ").strip()
        if not nama_input:
            break
        
        item_ditemukan = None
        for item in barang:
            if item["nama"].lower() == nama_input.lower():
                item_ditemukan = item
                break
        
        if not item_ditemukan:
            print("barang tidak ada")
            continue
        
        try:
            jumlah = int(input(f"Masukkan jumlah {item_ditemukan['nama']}: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            if jumlah > item_ditemukan["stok"]:
                print(f"Stok tidak mencukupi! Stok saat ini: {item_ditemukan['stok']}")
                continue
        except ValueError:
            print("Jumlah harus berupa angka!")
            continue

        nama_resmi = item_ditemukan["nama"]
        keranjang[nama_resmi] = keranjang.get(nama_resmi, 0) + jumlah

    if not keranjang:
        print("Tidak ada barang yang dibeli.")
        return

    total_harga = 0
    print("\n--- Rincian Pembelian ---")
    for nama_beli, qty in keranjang.items():
        for item in barang:
            if item["nama"] == nama_beli:
                subtotal = qty * item["harga"]
                total_harga += subtotal
                item["stok"] -= qty
                print(f"{nama_beli} ({qty} x Rp {item['harga']:,}) = Rp {subtotal:,}")
                break

    diskon = 0
    if total_harga > 200000:
        diskon = total_harga * 0.10
        print(f"\nSelamat! Anda mendapatkan Diskon 10%: Rp {int(diskon):,}")
    
    total_bayar = total_harga - diskon
    print(f"Total Harga : Rp {int(total_harga):,}")
    print(f"Total Bayar : Rp {int(total_bayar):,}")

while True:
    print('''
1. Tambah barang baru
2. Tampilkan barang & stok
3. Ubah harga/stok barang
4. Hapus barang
5. Transaksi 
    ''')

    pilihan_user = int(input("masukan pilihanmu: "))

    if pilihan_user == 1:
        kode_baru = input("masukan kode barang: ")
        nama_baru = input("masukan nama barang: ")
        harga_baru = int(input("masukan harga barang: "))
        stok_baru = int(input("masukan stok barang: "))

        add_data(data_barang, kode_baru, nama_baru, harga_baru, stok_baru)

    elif pilihan_user == 2:
        show_data(data_barang)

    elif pilihan_user == 3:
        kode_target = input("masukan kode barang yang mau diubah: ")
        harga_baru = int(input("masukan harga barang: "))
        stok_baru = int(input("masukan stok barang: "))

        change_data(data_barang, kode_target, harga_baru, stok_baru)

    elif pilihan_user == 4:
        kode_target = input("masukan kode barang yang mau diubah: ")

        delete_data(data_barang, kode_target)

    elif pilihan_user == 5:
        transaction(data_barang)
    