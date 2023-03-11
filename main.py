print("2 + 3")
print(2 + 3) # 2 dan 3 bisa disebut varibael
print("2" + "3")
# makna tanda pentik pada suatu program di python adalah, jadi 
# fungsi tanda petik yaitu untuk menampilkan sebuah program yang kita
# buat di dalam tanda petik...
print("\n")
bil1 = 10 # variabel = 3
bil2 = 5 # baris ke dua memiliki variabel yang bernama bil2  dan berjumlah 5
bil2 #tidak dapat tereksekusi sebelum menambahkan print
print(bil2) # dapat di eksekusi
jumlah = bil1 + bil2 # sedangkan baris keiga adalah adalah sebuah variabel yang berfungsi untuk 
# mengeksekusi variabel 1 dan 2 yaitu bil1 dan bil 2
jumlah # tidak dapat tereksekusi sebelum menambahkan print
print(jumlah) # dapat di eksekusi
print('\n')
data = [10,9,7,8,10,8,9]
print(data[1]) # 2.dihitung setelah 10
data[2] = 10
print(data)
data.append(9) # 1.append berfungsi sebagi penambah sebuah data pada ruang yang tersedia atau ruang setelah data yang sudah ada
print(data)

data =[10, 9, 7, 8, 10, 8]
indeks = 0 
for elemen in data:
    #indeks = indeks + 1 # jika diatas maka elemen dihitung / dimulai dengan akan satu sebagai awalan
    #print("Elemen ke", indeks, "=", elemen)
    indeks = indeks + 1 # jika indeks dibawah maka elemen dihitung dimulai dari nol
    
# ERROR
data = [10,9, 5, "Cindi", 4, "8"]
for x in data :
    try: 
        print(x/ 2)
    except:
        print("Error")