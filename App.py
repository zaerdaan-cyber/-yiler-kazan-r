import streamlit as st
import feedparser
import pandas as pd

st.title("İstanbul İlçe Haber Analiz Sistemi")

ilceler = [
"Adalar","Arnavutköy","Ataşehir","Avcılar","Bağcılar","Bahçelievler","Bakırköy",
"Başakşehir","Bayrampaşa","Beşiktaş","Beykoz","Beylikdüzü","Beyoğlu",
"Büyükçekmece","Çatalca","Çekmeköy","Esenler","Esenyurt","Eyüpsultan",
"Fatih","Gaziosmanpaşa","Güngören","Kadıköy","Kağıthane","Kartal",
"Küçükçekmece","Maltepe","Pendik","Sancaktepe","Sarıyer","Silivri",
"Sultanbeyli","Sultangazi","Şile","Şişli","Tuzla","Ümraniye","Üsküdar","Zeytinburnu"
]

rss = [
"https://www.trthaber.com/rss/manset.rss",
"https://www.ntv.com.tr/rss",
"https://www.cnnturk.com/feed/rss/all/news"
]

haberler=[]

for url in rss:
    feed=feedparser.parse(url)
    for entry in feed.entries:
        haberler.append({
            "baslik":entry.title,
            "link":entry.link
        })

sonuc=[]

for h in haberler:
    for ilce in ilceler:
        if ilce.lower() in h["baslik"].lower():
            sonuc.append({
                "ilce":ilce,
                "haber":h["baslik"],
                "link":h["link"]
            })

df=pd.DataFrame(sonuc)

st.dataframe(df)

st.bar_chart(df["ilce"].value_counts())
