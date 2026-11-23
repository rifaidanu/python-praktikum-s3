class buku:
    def init(self, id_buku, kode_buku, judul, penulis, tahun_terbit, kategori):
        self.id_buku = id_buku
        self.kode_buku = kode_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.kategori = kategori

    def __str__(self):
        return f"{self.id_buku} | {self.kode_buku} | {self.judul} | {self.penulis} | {self.tahun_terbit} | {self.kategori}"