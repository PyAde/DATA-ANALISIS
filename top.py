import requests
import pandas as pd 
from bs4 import BeautifulSoup
url = "https://www.jobs.id/lowongan-kerja?kata-kunci=programmer"
halaman_web = requests.get(url)
hasil = BeautifulSoup(halaman_web.content, 'html.parser')
lowkers = hasil.find_all(class_="single-job-ads")
posisi = []
instansi = []
gaji = []
lokasi = []
for info in lowkers :
  s1 = info.select("h3") 
  s2 = s1 [0].select("a")
  posisi.append(s2[0].get_text())
  lokasi.append(info.find("span", class_="location").get_text())
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
lowkers = pd.DataFrame({
  "Posisi": posisi,
  "Instansi": instansi,
  "Gaji":gaji,
  "Lokasi": lokasi
})
lowkers = lowkers.sort_values(by=['Gaji'], ascending=True)
lowkers

