mahasiswa = [
 	("Andi", "PTIK", 80),
 	("Siti", "Informatika", 90),
 	("Budi", "PTIK", 75),
 	("Citra", "Informatika", 88)
]

def hitung_data(data_mahasiswa):
    jumlah_data = len(data_mahasiswa)
    print(f"Data mahasiswa berjumlah {jumlah_data}")

def rata_rata(data_mahasiswa):
    total_nilai = sum(nilai for nama, prodi, nilai in data_mahasiswa)
    rata_nilai = total_nilai / len(data_mahasiswa)
    print(f"rata-rata nilai mahasiswa adalah {rata_nilai}")

def minmax_nilai(data_mahasiswa):
    mahasiswa_tertinggi = []
    mahasiswa_terendah = []

    nilai_tertinggi = max(nilai for nama, prodi, nilai in data_mahasiswa)
    nilai_terendah = min(nilai for nama, prodi, nilai in data_mahasiswa)

    for nama, prodi, nilai in data_mahasiswa:
        if nilai == nilai_tertinggi:
            mahasiswa_tertinggi.append(nama)

    for nama, prodi, nilai in data_mahasiswa:
        if nilai == nilai_terendah:
            mahasiswa_terendah.append(nama)

    print(f"Mahasiswa nilai tertinggi : {", ".join(mahasiswa_tertinggi)}")
    print(f"Mahasiswa nilai terendah : {", ".join(mahasiswa_terendah)}")

def lebih_dari_80(data_mahasiswa):
    print('Mahasiswa dengan nilai lebih dari 80 : ')
    for nama, prodi, nilai in data_mahasiswa:
        if nilai >= 80:
            print(nama)


while True:

    print('''
1. Menghitung seluruh data mahasiswa.
2. Menghitung rata-rata nilai.
3. Menampilkan mahasiswa dengan nilai tertinggi dan terendah.
4. Menampilkan mahasiswa yang memperoleh nilai ≥ 80  
5. keluar program
    ''')

    pilihan_user = int(input('masukan pilihan fitur: '))

    if pilihan_user == 1:
        hitung_data(mahasiswa)
    elif pilihan_user == 2:
        rata_rata(mahasiswa)
    elif pilihan_user == 3:
        minmax_nilai(mahasiswa)
    elif pilihan_user == 4:
        lebih_dari_80(mahasiswa)  
    elif pilihan_user == 5:
        break  
    else:
        print('menu tidak tersedia')