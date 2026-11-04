import datetime

nama = input("masukan nama anda: ")
umur = int(input("masukan umur anda: "))

tahun_sekarang = datetime.datetime.now().year

print(f"hallo nama anda {nama} berumur {umur} tahun")
print(f"tahun lahir anda adalah {tahun_sekarang - umur}")