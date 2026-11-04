inventori = {
    "Laptop": {"harga": 700000, "stok": 5},
    "Mouse": {"harga": 150000, "stok": 10},
    "Keyboard": {"harga": 250000, "stok": 7}
}

barang_dijual = {}

def tampilkan_barang():
    header_border = "+" + "-"*17 + "+" + "-"*15 + "+" + "-"*8 + "+"
    print("\n" + header_border)
    print(f"| {'Nama Barang':<15} | {'Harga':>13} | {'Stok':>6} |")
    print(header_border)
    for nama, detail in inventori.items():
        harga_str = f"Rp {detail['harga']:,}".replace(",", ".")
        print(f"| {nama:<15} | {harga_str:>13} | {detail['stok']:>6} |")
    print(header_border + "\n")

def beli_barang(list_barang, barang_dijual):

    while True:
        barang = input("masukan nama barang : ").capitalize()
        if barang == "Selesai":
            break

        jumlah = int(input("masukan jumlah : "))

        if barang in inventori:
            if jumlah <= inventori[barang]['stok']:
                inventori[barang]['stok'] -= jumlah
                if barang in barang_dijual:
                    barang_dijual[barang] += jumlah
                else:
                    barang_dijual[barang] = jumlah
            elif inventori[barang]['stok'] == 0:
                print('barang telah habis')
            else:
                print("jumlahnya kebanyakan tolong kurangi")
        else:
            print('barang tidak tersedia di inventori, silahkan masukan barang lain')

    for nama, jumlah in barang_dijual.items():
        print(f"{nama}, {jumlah}")

def hitung_diskon(daftar_barang, barang_terjual):
    total_harga = 0
    diskon = 0.1

    for nama, jumlah in barang_dijual.items():
        total_harga_barang = jumlah * inventori[nama]['harga']
        total_harga += total_harga_barang

    print(f"Total Harga : {total_harga}")
    if total_harga > 5000000:
        cetak_diskon = '10%'
        harga_diskon = total_harga*diskon
        total_harga -= harga_diskon
    else:
        cetak_diskon = '0%'
    print(f"Diskon : {cetak_diskon}")
    print(f"Harga akhir : {total_harga}")

while True:

    print('''
1. Tampilkan list barang
2. Beli barang
3. Keluar program
    ''')

    pilihan = int(input("masukan pilihan fitur : "))

    if pilihan == 1:
        tampilkan_barang()
    elif pilihan == 2:
        beli_barang(inventori, barang_dijual)
        hitung_diskon(inventori, barang_dijual)
    elif pilihan == 3:
        break