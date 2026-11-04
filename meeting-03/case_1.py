koleksi_lagu = []

def tambah_lagu(penyanyi, judul):
    koleksi_lagu.append({"judul": judul, "penyanyi": penyanyi})

def tampilkan_semua_lagu():
    print("DAFTAR SEMUA LAGU: ")
    for i in koleksi_lagu:
        print(i["judul"])

def hapus_lagu(judul_hapus):
    for i in koleksi_lagu:
        if i["judul"] == judul_hapus:
            koleksi_lagu.remove(i)

def cari_lagu(penyanyi_cari):
    for i in koleksi_lagu:
        if i["penyanyi"] == penyanyi_cari:
            print(f"Hasil pencarian: {i["judul"]}")

tambah_lagu("Olivia Rodrigo", "Stupid Song")
tambah_lagu("Barasuara", "Manusia")
tambah_lagu("Bernadya", "Laut Yang Tenang")
tambah_lagu("Lomba Sihir", "Selamanya")
tampilkan_semua_lagu()

hapus_lagu("Selamanya")

tampilkan_semua_lagu()

cari_lagu("Bernadya")