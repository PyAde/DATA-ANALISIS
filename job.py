

import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup

th = "https://www.jobstreet.co.id/id/job-search/computer-software-it-jobs/"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
info = hasil.find_all(class_="sx2jih0 zcydq8n lmSnC_0")

lokasi = []
posisi = []
instansi = []
gaji = []

for p in info:
    t1 = p.select("h1")
    t2 = t1[0].select("a")
    t3 = p.select("span")
    posisi.append(t2[0].get_text())
    instansi.append(p.find("span",class_="sx2jih0 zcydq84u _18qlyvc0 _18qlyvc1x _18qlyvc1 _18qlyvca").get_text())
    lokasi.append(p.find("span",class_="sx2jih0 iwjz4h1 zcydq84u zcydq80 zcydq8r").get_text())
    
    t1 = p.select("h1")
    t2 = t1[0].select("a")
    
lowkers = pd.DataFrame({
  "Posisi": posisi,
  "Instansi": instansi,
  "Lokasi":lokasi
})
lowkers