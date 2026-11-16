import streamlit as st
from User import User
import pandas as pd
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
veri=st.session_state
yol=Path(__file__).resolve().parent
st.header("Account Information", divider="blue" )
st.image(str(yol/"Gemini_Generated_Image_5y1rqv5y1rqv5y1r.jpg"), caption=" Exsmple of Bank Card", width=200)

if True:
    df=pd.read_csv(os.path.join(BASE_DIR, "user.csv"),names=["Name","ID","Password"])
    length=df.shape[0]
    with open(os.path.join(BASE_DIR, "user.csv"),"r", encoding="utf-8") as file:
         lines=file.readlines()
         liste=[]
         giris_sayısı=0
         for line in lines:
              name,id,ps=line.rstrip().split(",")
              if veri.ıd==id:
               if id not in liste:
                   liste.append(id)
                   giris_sayısı+=1
               elif id in liste:
                   giris_sayısı+=1
         df["Enterence"]=giris_sayısı
         row=df.iloc[length-1]
    st.dataframe(row)
                   

      
