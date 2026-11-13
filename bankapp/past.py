import streamlit as st
import pandas as pd

st.title("Past activites ")
veri=st.session_state
veri.past=True
if veri.past:
   with st.popover("Activites"):
    with open("balance.csv","r",encoding="utf-8") as file:
        liste=[]
        dict={}
        i1=["Withdraw","Deposit","Stock Purchase"]
        lines=file.readlines()
        for line in lines:
            balance,ıd,date,transaction=line.rstrip().split(",")
            liste.append({"bal":float(balance),"ıd":ıd,"date":date,"trans":transaction})
        for i in range(len(liste)):
         if veri.ıd==ıd:
           if i==0:
            st.write(f"{i+1}| {liste[i]['date']} | {liste[i]['trans']} | {liste[i]['bal']} | By {veri.name}   ")
           elif i>0:
            st.write(f"{i+1}| {liste[i]['date']} | {liste[i]['trans']} | {liste[i]['bal']-liste[i-1]['bal']} | By {veri.name}   ")
input1=st.text_input("İf you like my first app can you write down your instangram name?🫶❤️🫶 ")
if input1:
   url=f"https://www.instagram.com/{input1}/"
   with open("insta.csv","a",encoding="utf-8") as file:
      file.write(f"{url}\n")
      file.close()
   st.success("Thank Youuu 💕")

            
