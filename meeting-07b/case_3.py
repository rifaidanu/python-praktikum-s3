jadwal = [
 	("Senin", "08.00", "Pemrograman 1", "Lab 1"),
 	("Selasa", "10.00", "Basis Data", "Lab 2"),
	("Selasa", "15.00", "Kalkulus", "Lab 2"),
 	("Rabu", "13.00", "Multimedia", "Ruang 3")
]

def tampilkan_jadwal(jadwal):
	print(f"\n{'HARI':<11} {'WAKTU':<9} {'MATA KULIAH':<18} {'RUANGAN'}")
	print("-" * 49)
	for hari, waktu, mata_kuliah, tempat in jadwal:
		print(f"{hari:<11} {waktu:<9} {mata_kuliah:<18} {tempat}")
		
def cari_matkul(target_hari):
	hari_ditemukan = False
	print(f"\n{'MATA KULIAH':<18} {'RUANGAN':<11} {'WAKTU':<9}")
	print("-" * 36)
	for hari, waktu, mata_kuliah, tempat in jadwal:
		if hari == target_hari:
			print(f"{mata_kuliah:<18} {tempat:<11} {waktu:<9}")
			hari_ditemukan = True
	if not hari_ditemukan:
		print("Hari tidak ada")
	
def ruang_matkul(jadwal):
	print(f"\n{'MATA KULIAH':<18} {'RUANGAN':<8}")
	print("-" * 26)
	for hari, waktu, mata_kuliah, tempat in jadwal:
		print(f"{mata_kuliah:<18} {tempat:<8}")

while True:
	print('''
Fitur Program
1. Tampilkan semua jadwal
2. Cari jadwal by hari
3. Tampilkan mata kuliah dan ruang
	''')

	pilihan_user = int(input("masukan pilihan : "))

	if pilihan_user == 1:
		tampilkan_jadwal(jadwal)
		print("\n")
	elif pilihan_user == 2:
		print("\nCari matkul berdasarkan hari")
		target_hari = input("Masukan Hari : ").capitalize()
		cari_matkul(target_hari)
	elif pilihan_user == 3:
		ruang_matkul(jadwal)	
	else:
		break