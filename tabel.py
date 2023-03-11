import requests
# import request merupakan sebuah packages yang dimana menggunakan library request. Fungsi request
# ini untuk menngirim permintaan kepada http ke sebuah url atau untuk mengambil data dari API atau
# situs web lain dan memprosesnya
import pandas as pd
# pandas merupakan sebuah library python yang menyediakan struktur data dan analisis data yang mudah digunakan.
# struktur data pandas disebut DataFrame. Fungsi pandas yaitu
# digunakan kali ini yaitu membentuk data menjadi data dengan menggunakan
# DataFrame 
from bs4 import BeautifulSoup
# BeautifulSoup adalah library python yang digunkan untuk mengambil data dari sebuah struktur HTML pada sebuah website
# dan bisa mengambil struktur XML
url = "https://www.jobs.id/lowongan-kerja?kata-kunci=programmer"
# url merupakan sebuah variabel yang menyimpan sebuah link yang ingin di scraping
halaman_web = requests.get(url)
# halaman_web menggunakan library request untuk mengambil data dari link pada variabel url
hasil = BeautifulSoup(halaman_web.content, 'html.parser')
# hasil menggunakan library BeatifulSoup untuk mengambil data html pada variabel halaman_web
lowkers = hasil.find_all(class_="single-job-ads")
# lowkers adalah variabel yang mencari sebuah elemen div yang menggunakan class single-job-ads untuk mendapatkan
# informasi data yang diperlukan
posisi = []
instansi = []
gaji = []
lokasi = []
# data ini kemudian berbentuk array supaya informasi data mudah untuk dikelompokan
# awal untuk mencari posisi dari suatu perkejaan
for info in lowkers :
  s1 = info.select("h3") 
  s2 = s1 [0].select("a")
  posisi.append(s2[0].get_text())
  #akhir mencari posisi
  # awal mencari lokasi perkejaan
  lokasi.append(info.find("span", class_="location").get_text())
  #akhir mencari lokasi perkejaan
  # awal untuk mencari instansi perkejaan
  s1 = info.select("p")
  s2 = s1[0].select("a")
  try:
    instansi.append(s2[0].get_text())
  except:
    instansi.append("-")
  # akhir instansi perkejaan
  # awal mencari gaji
  s2 = s1[1].select("span")
  try:
    gaji.append(s2[1].get_text())
  except:
    gaji.append(s2[0].get_text())
  # akhir mencari gaji
# data kemudian berbentuk tabel dengan batuan DataFrame
lowkers = pd.DataFrame({
  "Posisi": posisi,
  "Instansi": instansi,
  "Gaji":gaji,
  "Lokasi": lokasi
})
# Mencari gaji dari yang terendah dan terbesar menggunakan ascending dengan tipe data Boolean
lowkers = lowkers.sort_values(by=['Gaji'], ascending=True)
lowkers
# akhir data berbentuk tabel
