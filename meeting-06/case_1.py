data_mahasiswa = []

while True:
    nama = input("masukan nama mahasiswa : ")
    prodi = input("masukan nama prodi : ").lower()
    ipk = float(input("masukan IPK : "))

    mahasiswa = [nama, prodi, ipk]
    data_mahasiswa.append(mahasiswa)

    pilihan = input('ketika "selesai" jika sudah selesai input "enter" jika lanjut: ')
    if pilihan == "selesai":
        break

ipk_mahasiswa = []
ipk_ptik = []

for i in data_mahasiswa:
    ipk_mahasiswa.append(i[2])

for i in data_mahasiswa:
    if i[1] == "ptik":
        ipk_ptik.append(i[2])

ipk_average = sum(ipk_ptik) / len(ipk_ptik)
max_ipk = max(ipk_mahasiswa)
min_ipk = min(ipk_mahasiswa)

print(f"IPK prodi PTIK : {ipk_average}")
print(f"IPK tertinggi : {max_ipk}")
print(f"IPK terendah : {min_ipk}")