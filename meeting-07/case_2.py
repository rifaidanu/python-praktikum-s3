mahasiswa = {
    "Andi": {"prodi": "PTIK", "ipk": 3.8},
    "Siti": {"prodi": "Informatika", "ipk": 3.9},
    "Budi": {"prodi": "PTIK", "ipk": 3.6}
}

def tampilkan_mahasiswa(kumpulan_mahasiswa):
    print(f"\n{"Nama":<10} {"Prodi":15} {"IPK":8}")
    print("-"*35)
    for nama, identitas in kumpulan_mahasiswa.items():
        print(f"{nama:<10} {identitas["prodi"]:15} {identitas["ipk"]:8.2}")

def hitung_nilai(kumpulan_mahasiswa):
    kumpulan_ipk = []

    for ipk in kumpulan_mahasiswa.values():
        kumpulan_ipk.append(ipk['ipk'])

    average = sum(kumpulan_ipk) / len(kumpulan_ipk)

    nama_tertinggi = max(kumpulan_mahasiswa, key=lambda nama: kumpulan_mahasiswa[nama]['ipk'])
    nama_terendah = min(kumpulan_mahasiswa, key=lambda nama: kumpulan_mahasiswa[nama]['ipk'])

    min_value = min(kumpulan_ipk)
    max_value = max(kumpulan_ipk)

    print(f"rata-rata IPK mahasiswa : {average}")
    print(f"IPK terendah : {nama_terendah} {min_value}")
    print(f"IPK tertinggi : {nama_tertinggi} {max_value}")

def kelompokkan_prodi(kumpulan_mahasiswa):
    # 1. Olah data: kelompokkan nama & IPK per prodi
    prodi_dict = {}
    for nama, data in kumpulan_mahasiswa.items():
        prodi = data["prodi"]
        if prodi not in prodi_dict:
            prodi_dict[prodi] = []
        prodi_dict[prodi].append({"nama": nama, "ipk": data["ipk"]})
    return prodi_dict

def tampilkan_kelompok_prodi_tabel(kumpulan_mahasiswa):
    prodi_dict = kelompokkan_prodi(kumpulan_mahasiswa)
    
    for prodi, daftar_mhs in prodi_dict.items():
        print(f"\n PRODI: {prodi} ({len(daftar_mhs)} Mahasiswa)")
        print(f"{'No.':<6}{'Nama Mahasiswa':<20}{'IPK':<10}")
        print("-" * 45)
        for idx, mhs in enumerate(daftar_mhs, start=1):
            print(f"{idx:<6}{mhs['nama']:<20}{mhs['ipk']:<10.2f}")

while True:

    print('''
1. Tampilkan data semua mahasiswa
2. Rata-rata IPK semua mahasiswa
3. Kelompok prodi mahasiswa
    ''')

    pilihan_user = int(input("masukan pilihan anda: "))

    if pilihan_user == 1:
        tampilkan_mahasiswa(mahasiswa)
    elif pilihan_user == 2:
        hitung_nilai(mahasiswa)
    elif pilihan_user == 3:
        tampilkan_kelompok_prodi_tabel(mahasiswa)
    else:
        break
