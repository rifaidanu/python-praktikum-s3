teks = "Pratikum Pemrograman"
vokal = "AIUEOaiueo"

jumlah_vokal = 0

for char in teks:
    if char in vokal:
        jumlah_vokal+=1

print(jumlah_vokal)