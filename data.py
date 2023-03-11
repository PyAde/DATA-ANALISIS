import pandas 
# ternyata begitu

# ALTERNATIF
#data = {"DATA" :[10,9,8,9,10,8,7,4],
        #"Siswa": ["Budi", "Cindy", "Akmal", "Ahmad", "Adel","Dedy", "Windah",
                #"Yusuf"]
#}

#sesad modul

#total = pandas.DataFrame(data)

#print(total)

data = [10, 9, 8, 9, 10]
siswa = ["andi","adel","cindy","ahmad","imam"]

nilai = pandas.DataFrame({
        "Nama": siswa,
        "Nilai":data
})

print(nilai)