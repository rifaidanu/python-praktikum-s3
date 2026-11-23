class Peminjaman:
    def init(self, id_peminjaman, id_anggota, id_petugas, tanggal_pinjam, tanggal_kembali, status):
        self.id_peminjaman = id_peminjaman
        self.id_anggota = id_anggota
        self.id_petugas = id_petugas
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def __str__(self):
        return f"{self.id_peminjaman} | {self.id_anggota} | {self.id_petugas} | {self.tanggal_pinjam} | {self.tanggal_kembali} | {self.status}"