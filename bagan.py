import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
# ambil data lowongan kerja dari website jobs.id
url = "https://www.jobs.id/lowongan-kerja-programmer?kata-kunci=programmer"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
lowkers = soup.find_all(class_="single-job-ads")
posisi = []
instansi = []
gaji = []
lokasi = []
for info in lowkers:
    s1 = info.select("h3")
    s2 = s1[0].select("a")
    posisi.append(s2[0].get_text())
    lokasi.append(info.find("span",class_="location").get_text())
    s1 = info.select("p")
    s2 = s1[0].select("a")
    try:
        instansi.append(s2[0].get_text())
    except:
        instansi.append("-")
    s2 = s1[1].select("span")
    try:
        gaji.append(s2[1].get_text())
    except:
        gaji.append(s2[0].get_text())
# buat dataframe dari informasi lowongan kerja
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
# menghapus sebuah nilai numeric pada Gaji
lowkers = lowkers.dropna(subset=["Gaji"])
lowkers = lowkers[lowkers["Gaji"] > 0]
# hitung rata-rata gaji dalam juta rupiah
rata_rata_gaji = lowkers["Gaji"].mean() / 1000000
# urutkan data berdasarkan gaji terkecil dan terbesar
lowkers = lowkers.sort_values(by=["Gaji"], ascending=True)
# Mencari nilai tengah gaji
median_gaji = lowkers["Gaji"].median() / 1000000
# membentuk data menggunakan diagram batang
fig = px.bar(lowkers, x='Posisi', y=lowkers['Gaji'] / 1000000, color='Lokasi', title='Gaji Programmer di jobs.id Rata-rata gaji: Rp{:.2f} juta'.format(rata_rata_gaji))
# tambahkan teks median pada diagram
fig.add_annotation(dict(text='Nilai Tengah Gaji: {:.2f} juta'.format(median_gaji), x=0, y=-3, font_size=16, showarrow=False))
fig.show()
