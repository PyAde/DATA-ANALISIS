import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup

th = "https://karir.com/search?context=welcome_main_search&q=programmer&location=&IREFERRER=direct&LREFERRER=direct&ILANDPAGE=https%253A%2F%2Fkarir.com%2F&VISITS=1"
halaman = requests.get(th)
hasil = BeautifulSoup(halaman.content, 'html.parser')
info = hasil.find_all(class_="row opportunity-box")

lokasi = []
posisi = []
instansi = []
gaji = []
umur = []

for p in info:
  s1 = p.select("a")
  s2 = s1[0].select("h4")
  posisi.append(s2[0].get_text())
  lokasi.append(p.find("span", class_="tdd-location").get_text())
  umur.append(p.find("span", class_="tdd-experience").get_text())
  
  s3 = p.select("p")
  s4 = s3[0].select("span")
  
  try:
    xgaji = s4[1].get_text()
  except:
    xgaji = s4[0].get_text()
  xgaji = xgaji.replace(".","")
  if(xgaji == "Gaji Kompetitif"):
    xgaji = 0
  gaji.append(xgaji)
  
  info = pd.DataFrame({
    "Posisi": posisi,
    "Gaji": gaji,
    "Lokasi": lokasi,
    "Umur":umur,
    
  })
  
  
