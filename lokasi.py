import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup

th = "https://www.jobs.id/lowongan-kerja?kata-kunciprogrammer"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
lowkers = hasil.find_all(class_="single-job-ads")


posisi = []
instansi = []
gaji = []
lokasi = []

import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup

th = "https://www.jobs.id/lowongan-kerja?kata-kunciprogrammer"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
lowkers = hasil.find_all(class_="single-job-ads")

posisi = []
instansi = []
gaji = []
lokasi = []

for p in lowkers :
  t1 = p.select("h3")
  t2 = t1[0].select("a")
  posisi.append(t2[0].get_text())
  lokasi.append(p.find("span",class_="location").get_text())

  t1 = p.select("p")
  t2 = t1[0].select("a")

  try:
    instansi.append(t2[0].get_text())
  except:
    instansi.append("-")
  t2 = t1[1].select("span")
  try:
    xgaji = t2[1].get_text()
  except:
    xgaji = t2[0].get_text()
  xgaji = xgaji.replace(".","")
  if (xgaji=="Gaji Dirahasiakan"):
    xgaji = 0 
  gaji.append(xgaji);
  
  lowkers = pd.DataFrame({
  "Posisi": posisi,
  "Instansi": instansi,
  "Gaji":gaji,
  "Lokasi":lokasi
})
print(lowkers)
