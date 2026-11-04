class Dosen:
    def __init__(self, nama: str, nidn: str, mata_kuliah: str):
        self.nama = nama
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah


    def info(self):
        print(f'''
        Nama : {self.nama}
        NIDN : {self.nidn}
        Mata Kuliah : {self.mata_kuliah}
        ''')

    def update_mata_kuliah(self, mata_kuliah_baru: str):
        self.mata_kuliah_baru = mata_kuliah_baru
        
        self.mata_kuliah = mata_kuliah_baru

vearen = Dosen("vearen", "123", "Pemrograman")
dexa = Dosen("Dexa", "7669898", "Pemrograman Berorientasi Objek")
rosihan = Dosen("Rosihan", "9849343", "Pemrograman Dasar")

vearen.info()
vearen.update_mata_kuliah("English")
vearen.info()