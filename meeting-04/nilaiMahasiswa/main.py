import hitung
import laporan
import predikat

nama = "Dion"
tugas = 90
uts = 100
uas = 80

nilai_akhir = hitung.hitung_nilai(tugas, uts, uas)
predikat_nilai = predikat.predikat_nilai(nilai_akhir)

daftar_nilai = [80, 85, 90, 75]
rata_kelas = hitung.rata_rata(daftar_nilai)

laporan.cetak_nilai(nama, tugas, uts, uas, nilai_akhir, predikat_nilai)
laporan.cetak_average(rata_kelas)