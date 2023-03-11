# Latihan 4
bil1= 10
print(bil1)
bil1 = 5
print(bil1)
#jawaban nomer 1
#10 dan 5
#jawaban nomer 2
# iya, karena ada dua jumlah nilai pada satu variabel yaitu bil1
# jadi pada baris ke empat merupakan sebuah perintah untuk
# menghasilkan output dari bil1 yang sudah di perbarui
# nilainya yaitu 5. Hasil 5 tersebut terjadi karena
# variabel yang pada baris pertama diperbarui nilainya
# menjadi 5 pada baris ke tiga atau print akan mencetak
# sebuah variabel yang  baru dibuat
#Latihan 5
data = [10, 9, 7, 8, 10, 8]
print(data[1])
data = [10]
print(data)
data.append(9)
print(data)
# jawaban nomer 1
# 9
# jawaban nomer 2
# karna data berbentuk array, sedangkan array dimulai dari
# angka 0(nol). 
#Latihan 6
data = [10, 9, 7, 8, 10, 8]
indeks = 0
for elemen in data:
  indeks = indeks + 1
  print("Elemen ke", indeks,"=",elemen)
#jawaban nomer 1
# karena supaya nilai dari elemen berubah atau ditambah 1 setiap perulangan
# jawaban nomer 2
# berarti jika indeks = indeks + 2 maka,setiap perulangan nilai dari elemen ditambah 2
# jawaban nomer 3
# berarti indeks dimulai dari 1 bukan dari 0
#Elemen ke 1 = 10
#Elemen ke 2 = 9
#Elemen ke 3 = 7
#Elemen ke 4 = 8
#Elemen ke 5 = 10
#Elemen ke 6 = 8
# latihan 7
#  while merupakan sebuah perulangan yang digunakan jika suatu kondisi
# tersebut sesuai atau terpenuhi
# Latihan 8
data = [10, 9, "Cindi", 4, "8"]
for x in data:
  print(x/2)
# jawaban nomer 8, error tersebut terjadi karena, sebuah tipe data berbentuk str tidak dapat
# dibagi dengan tipe data int
# latihan 9
data = [10, 9, "Cindi", 4, "8"]
for x in data:
  try:
    print(x/2)
  except:
    print("Bukan bilangan")
# tiga bilangan
# Latihan 10
# branch if atau elif-else digunakan untuk menentukan suatu kondisi
# tertentu pada suatu program yang dibuat