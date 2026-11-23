class DetailPeminjaman:
    def init(self, id_detail, id_peminjaman, id_buku, jumlah):
        self.id_detail = id_detail
        self.id_peminjaman = id_peminjaman
        self.id_buku = id_buku 
        self.jumlah = jumlah   

    def __str__(self):
        return f"{self.id_detail} | {self.id_peminjaman} | {self.id_buku} | {self.jumlah}"