data_pegawai = [
    {"nip": "PG001", "nama": "Rina", "jabatan": "Staf Administrasi", "gaji": 4500000},
    {"nip": "PG002", "nama": "Budi", "jabatan": "Manajer", "gaji": 8500000},
    {"nip": "PG003", "nama": "Siti", "jabatan": "Supervisor Keuangan", "gaji": 6500000},
    {"nip": "PG004", "nama": "Andi", "jabatan": "Software Engineer", "gaji": 7500000},
    {"nip": "PG005", "nama": "Dewi", "jabatan": "Desainer Grafis", "gaji": 5200000},
    {"nip": "PG006", "nama": "Hendra", "jabatan": "Staf Pemasaran", "gaji": 4800000},
    {"nip": "PG007", "nama": "Maya", "jabatan": "Kepala Cabang", "gaji": 12000000},
    {"nip": "PG008", "nama": "Rizky", "jabatan": "Analis Data", "gaji": 7000000},
    {"nip": "PG009", "nama": "Nita", "jabatan": "Spesialis HRD", "gaji": 5800000},
    {"nip": "PG010", "nama": "Fajar", "jabatan": "Dukungan Teknis", "gaji": 4200000}
]

def create_data(pegawai, nip_baru, nama_baru, jabatan_baru, gaji_baru: int):
    pegawai.append({"nip":nip_baru, "nama":nama_baru, "jabatan":jabatan_baru, "gaji":gaji_baru})
    read_data(pegawai)

def read_data(pegawai):
    print(f"{"NIP":<8} {"NAMA":<8} {"JABATAN":<20} {"GAJI":<8}")
    print("-"*44)
    for i in pegawai:
        print(f"{i["nip"]:<8} {i["nama"]:<8} {i["jabatan"]:<20} {i["gaji"]:<8}")

def update_data(pegawai, nip_target, jabatan_baru, gaji_baru):
    for data in pegawai:
        if data["nip"] == nip_target:
            data["jabatan"] = jabatan_baru
            data["gaji"] = gaji_baru
        
    # read_data(pegawai)

def delete_data(pegawai, nip_target):
    for data in pegawai:
        if data["nip"] == nip_target:
            pegawai.remove(data)

    read_data(pegawai)

def hitung_rata(pegawai):
    total = sum(i["gaji"] for i in pegawai)
    jumlah_karyawan = len(pegawai)

    rata_rata = total / jumlah_karyawan
    print(f"rata-rata gaji pegawai adalah : {rata_rata}")

while True:
    print(
'''pilihan user :
1. Tambah data baru
2. Tampilkan semua data
3. Ubah data
4. Hapus data
5. Hitung rata-rata gaji
    ''')

    pilihan_user = int(input("masukan pilihan : "))

    if pilihan_user == 1:
        nip_baru = input("masukan NIP : ")
        nama = input("masukan nama : ")
        jabatan = input("masukan jabatan : ")
        gaji = int(input("masukan gaji : "))

        create_data(data_pegawai, nip_baru, nama, jabatan, gaji)
    elif pilihan_user == 2:
        read_data(data_pegawai)
    elif pilihan_user == 3:
        nip_target = input("masukan NIP : ")
        jabatan_baru = input("masukan jabatan baru : ")
        gaji_baru = int(input("masukan gaji baru : "))

        update_data(data_pegawai, nip_target, jabatan_baru, gaji_baru)
    elif pilihan_user == 4:
        nip_dihapus = input("masukan NIP pegawai yang mau dihapus : ")

        delete_data(data_pegawai, nip_dihapus)
    elif pilihan_user == 5:
        hitung_rata(data_pegawai)
