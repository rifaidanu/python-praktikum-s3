koordinat = [(0,0), (2,3), (4,1), (-1,5)]
jumlah_awal = len(koordinat)

def tampilkan_titik(data_koordinat):
    print("Daftar Titik : ")
    for titik in data_koordinat:
        print(titik)

def tambahin_titik(data_koordinat):
    while True:
        x = int(input("masukan titik x baru : "))
        y = int(input("masukan titik y baru : "))

        data_koordinat.append((x,y))

        if (x,y) in data_koordinat:
            print("Data Berhasil Masuk")
        else:
            print("Data Tidak Masuk")

        jumlah_akhir = len(data_koordinat)
        jumlah_data_baru = jumlah_akhir - jumlah_awal

        next_input = input("lanjut masukan koordinat (yes/no) : ").lower()

        if next_input == 'yes':
            pass
        elif next_input == 'no' and jumlah_data_baru < 2:
            print('masukan minimal 2 koordinat baru')
            pass
        elif next_input == 'no':
            break
        else:
            print('pilihan tidak ada')

def hitung_titik(data_koordinat):
    jumlah_titik = len(data_koordinat)
    print(f"Jumlah Titik : {jumlah_titik}")

def cari_titik(data_koordinat, koordinat_dicari):
    if koordinat_dicari in data_koordinat:
        print(f"koordinat {koordinat_dicari} ditemukan, berada di index {koordinat.index(koordinat_dicari)}")
    else:
        print('koordinat tidak ada')

while True:
    print('''
1. Tampilkan semua titik
2. Tambahkan titik
3. Hitung jumlah titik
4. Cari titik
5. Keluar program
    ''')

    pilihan_user = int(input('masukan pilihan fiturmu (hanya angka) : '))

    if pilihan_user == 1:
        tampilkan_titik(koordinat)
    elif pilihan_user == 2:
        tambahin_titik(koordinat)
    elif pilihan_user == 3:
        hitung_titik(koordinat)
    elif pilihan_user == 4:
        koordinat_x_dicari = int(input('masukan koordinat x: '))
        koordinat_y_dicari = int(input('masukan koordinat y: '))

        koordinat_dicari = (koordinat_x_dicari, koordinat_y_dicari)
        cari_titik(koordinat, koordinat_dicari)
    elif pilihan_user == 5:
        break