import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
from statistics import median

# ambil data lowongan kerja dari website
url = "https://www.jobs.id/lowongan-kerja-programmer?kata-kunci=programmer"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
lowkers = soup.find_all(class_="single-job-ads")

# ekstrak informasi posisi, instansi, gaji, dan lokasi
posisi = []
instansi = []
gaji = []
lokasi = []

for lowker in lowkers:
    t1 = lowker.select("h3")
    t2 = t1[0].select("a")
    posisi.append(t2[0].get_text())
    lokasi.append(lowker.find("span",class_="location").get_text())
        
    t1 = lowker.select("p")
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

# buat dataframe dari informasi lowongan kerja
lowkers_df = pd.DataFrame({
    "Posisi": posisi,
    "Instansi": instansi,
    "Gaji": gaji,
    "Lokasi": lokasi
})

# fungsi untuk mengonversi nilai gaji dari string ke float
def convert_gaji(gaji):
    try:
        return float(gaji.replace("Rp", "").replace(".", "").strip())
    except:
        return None

# konversi kolom "Gaji" menjadi float
lowkers_df["Gaji"] = lowkers_df["Gaji"].apply(convert_gaji)

# hapus nilai kosong dan non-numerik pada kolom "Gaji"
lowkers_df = lowkers_df.dropna(subset=["Gaji"])
lowkers_df = lowkers_df[lowkers_df["Gaji"] > 0]

# hitung rata-rata dan median gaji dalam juta rupiah
rata_rata_gaji = lowkers_df["Gaji"].mean() / 1000000
median_gaji = median(lowkers_df["Gaji"]) / 1000000

# urutkan data berdasarkan gaji terkecil dan terbesar
lowkers_df = lowkers_df.sort_values(by=["Gaji"], ascending=True)

# buat diagram lingkaran untuk menampilkan informasi posisi, gaji, dan lokasi
# hitung median gaji dalam juta rupiah
median_gaji = lowkers_df["Gaji"].median() / 1000000

# buat diagram lingkaran untuk menampilkan informasi posisi, gaji, dan lokasi
fig = px.pie(lowkers_df, values='Gaji', names='Posisi', hover_data=['Lokasi'], title='Gaji Rata-Rata Programmer di jobs.id adalah Rp{:.2f} juta'.format(rata_rata_gaji))

# tambahkan teks median pada diagram
fig.add_annotation(dict(text='Median: {:.2f} juta'.format(median_gaji), x=0, y=1, font_size=16, showarrow=False))

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
