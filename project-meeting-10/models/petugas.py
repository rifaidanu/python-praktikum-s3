class Petugas:
    def init(self, id_petugas, nama_petugas, username):
        self.id_petugas = id_petugas
        self.nama_petugas = nama_petugas
        self.username = username
            
    def __str__(self):
        return f"{self.id_petugas} | {self.nama_petugas} | {self.username}"