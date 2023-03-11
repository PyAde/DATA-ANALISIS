import requests
import pandas as pd
import plotly.express as px
# fungsi library plotly adalah untuk membentuk diagram lingkaran atau batang
from bs4 import BeautifulSoup
# ambil data lowongan kerja dari website
url = "https://www.jobs.id/lowongan-kerja-programmer?kata-kunci=programmer"
halaman_web = requests.get(url)
hasil = BeautifulSoup(halaman_web.content, 'html.parser')
lowkers = hasil.find_all(class_="single-job-ads")
# ekstrak informasi posisi, instansi, gaji, dan lokasi
posisi = []
instansi = []
gaji = []
lokasi = []
for info in lowkers:
    t1 = info.select("h3")
    t2 = t1[0].select("a")
    posisi.append(t2[0].get_text())
    lokasi.append(info.find("span",class_="location").get_text())
        
    t1 = info.select("p")
    t2 = t1[0].select("a")
    try:
        instansi.append(t2[0].get_text())
    except:
        instansi.append("-")
    t2 = t1[1].select("span")
    try:
        gaji.append(t2[1].get_text())
    except:
        gaji.append(t2[0].get_text())
        
lowkers = pd.DataFrame({
    "Posisi": posisi,
    "Instansi": instansi,
    "Gaji": gaji,
    "Lokasi": lokasi
})
# menerapkan konsep OOP atau yang bisa disebut Object Oriented Programming Python
# untuk mengubah nilai gaji yang string menjadi float
def ubah_gaji(gaji):
    try:
        return float(gaji.replace("Rp", "").replace(".", "").strip())
    except:
        return None
# konversi kolom Gaji menjadi sebuah tipe data float
lowkers["Gaji"] = lowkers["Gaji"].apply(ubah_gaji)
# menghapus nilai numeric pada Gaji
lowkers = lowkers.dropna(subset=["Gaji"])
lowkers = lowkers[lowkers["Gaji"] > 0]
# program menghitung rata-rata nilai gaji
rata_rata_gaji = lowkers["Gaji"].mean() / 1000000
#print rata-rata gaji
#"Rata-rata gaji: Rp{:.2f} juta".format(rata_rata_gaji)
# urutkan data berdasarkan gaji terkecil dan terbesar menggunakan kosenp
# ascending 
lowkers = lowkers.sort_values(by=["Gaji"], ascending=True)
# buat diagram lingkaran untuk menampilkan informasi posisi, gaji, dan lokasi
fig = px.pie(
    lowkers, values='Gaji', names='Posisi', hover_data=['Lokasi'], title='Gaji Rata-Rata Programmer di jobs.id adalah Rp{:.2f} juta'
    .format(rata_rata_gaji))
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
