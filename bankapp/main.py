from typing import cast
from User   import User
import streamlit as st
import time
from datetime import datetime,date
import pandas as pd
import yfinance as yf
import math
import json
from latest import late as lt
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


yol=Path(__file__).resolve().parent
stock1 = [
    # ABD 
    " AAPL - Apple Inc.",
    "🪟 MSFT - Microsoft Corporation",
    "🎮 NVDA - NVIDIA Corporation",
    "📦 AMZN - Amazon.com, Inc.",
    "🔍 GOOGL - Alphabet Inc.",
    "♾️ META - Meta Platforms, Inc.",
    "🚗 TSLA - Tesla, Inc.",
    "💻 AMD - Advanced Micro Devices, Inc.",
    "🎬 NFLX - Netflix, Inc.",
    "🏦 JPM - JPMorgan Chase & Co.",
    
    # Borsa İstanbul 
    "✈️ THYAO.IS - Türk Hava Yolları Anonim Ortaklığı",
    "🛡️ ASELS.IS - Aselsan Elektronik Sanayi ve Ticaret A.Ş.",
    "⛽ TUPRS.IS - Türkiye Petrol Rafinerileri A.Ş.",
    "🏢 KCHOL.IS - Koç Holding A.Ş.",
    "🏦 AKBNK.IS - Akbank T.A.Ş.",
    "🏦 GARAN.IS - Türkiye Garanti Bankası A.Ş.",
    "🏦 ISCTR.IS - Türkiye İş Bankası A.Ş.",
    "🏦 YKBNK.IS - Yapı ve Kredi Bankası A.Ş.",
    "🛒 BIMAS.IS - BİM Birleşik Mağazalar A.Ş.",
    "🏗️ EREGL.IS - Ereğli Demir ve Çelik Fabrikaları T.A.Ş.",
    "🚙 FROTO.IS - Ford Otomotiv Sanayi A.Ş.",
    "🪟 SISE.IS - Türkiye Şişe ve Cam Fabrikaları A.Ş.",
    "📱 TCELL.IS - Turkcell İletişim Hizmetleri A.Ş.",
    "🧪 SASA.IS - Sasa Polyester Sanayi A.Ş.",
    
    
    "🇹🇷 XU100.IS - BIST 100 Index",
    "🇺🇸 ^GSPC - S&P 500",
    "📈 ^IXIC - NASDAQ Composite",
    "🪙 GC=F - Gold Futures",
    "💵 TRY=X - USD/TRY Exchange Rate"
]



veri=st.session_state
if "fin" not in veri:
   veri.fin=[]
if "past" not in veri:
   veri.past=False
if "liste" not in veri:
    veri.liste=[]
if "step" not in veri:
    veri.step = 0
if "deposit" not in veri:
    veri.deposit = False
if "withd" not in veri:
    veri.withd = False
if "graph" not in veri:
    veri.graph = False
if "stock" not in veri:
    veri.stock = False
# session_state datas

@st.dialog("Stock request")
def stock():
          code=st.text_input("Enter the stock code (ex,GGL MRT)")
          if code:
           frame=yf.Ticker(code.upper())
          if  code:
           info1=frame.info
           st.write(f"Current value of **{info1.get('longName')}**: {info1.get('currentPrice')}")
           n4=st.number_input("Enter number of stock ", step=1)
           if veri.balance-(n4*info1.get('currentPrice'))>-1000000000 and n4:
              st.write(f"Total Cost:**{n4*info1.get('currentPrice')}**. İf you sure enter **'Buy'** button")
              if st.button("Buy"):
                 veri.balance-=n4*info1.get('currentPrice')
                 with open(os.path.join(BASE_DIR, "balance.csv"),"a",encoding="utf-8") as file:
                    file.write(f"{veri.balance},{veri.ıd},{date.today()},Stock-Purchase({info1.get('longName')})\n")
                 st.empty()
                 st.success("Sucessufly make transaction")
                 time.sleep(5)
                 st.empty()

                 veri.stock=False
                 st.rerun()
#showing balance and making transactions         
def acnt_page(position):
 with position:
  
   lister=[]
   history=[]  
   col1,col2,col3,col4=st.columns([1,1,1,3])
   with col1:
    button6=st.button("➖Whitdraw",type="tertiary")
   with col2:
    button7=st.button("➕Deposit",type="tertiary")
   with col3:
    button23=st.button("💰Buy Stock",type="primary")
   with col4:
      button20=st.button("📈Show  balance change",type="secondary")
   with open(os.path.join(BASE_DIR, "balance.csv"),"r",encoding="utf-8") as file:
      lines=file.readlines()
      if "balance" not in veri:
         veri.balance=0.0
      if lines:
       for line in lines:
         balance3,idd,times,trans=line.rstrip().split(",")
         if veri.ıd==idd:
            lister.append(float(balance3))
      if lister:
       veri.balance=lister[-1]
      else:
         veri.balance=0
   if button6:
         veri.withd=True
   if veri.withd:
          n= st.number_input("Enter amount of money for transaction")
          if veri.balance-n<-10000000000 and n:
            st.empty()
            st.error(" Can't make transaction: Excess your limit ")
            time.sleep(5)
            st.empty()
          elif n:
           veri.balance-=n
           with open(os.path.join(BASE_DIR, "balance.csv"),"a",encoding="utf-8") as file:
            file.write(f"{veri.balance},{veri.ıd},{date.today()},Withdraw\n")
           veri.withd=False
           st.rerun()
   if button7:
         veri.deposit=True
   if veri.deposit:        
          n1=st.number_input("Enter amount of money for transaction")
          if n1>1000000 and n1:
            st.write("if you want make this transaction please enter 'Submit' button")
            if st.button("Confirm Deposit"):
               veri.balance+=n1
               with open(os.path.join(BASE_DIR, "balance.csv"),"a",encoding="utf-8") as file:
                file.write(f"{veri.balance},{veri.ıd},{date.today()},Deposit\n")
               veri.deposit=False
               st.rerun()
          elif n1 and n1<=1000000:
               veri.balance+=n1
               with open(os.path.join(BASE_DIR, "balance.csv"),"a", encoding="utf-8") as file:
                file.write(f"{veri.balance},{veri.ıd},{date.today()},Deposit\n")
               veri.deposit=False
               st.rerun()
   if button20:
    veri.graph=True
   if veri.graph:
     with open(os.path.join(BASE_DIR, "balance.csv"),"r",encoding="utf-8") as file:
      lines=file.readlines()
      for line in lines:
        balance,ıd,date1,transaction=line.rstrip().split(",")
        if veri.ıd==ıd:
            history.append([float(balance),date1])       
      df=pd.DataFrame(sorted(history,key=lambda x:x[1]) ,columns=["Balance","Date"])
      st.line_chart(data=df, x='Date', y='Balance', y_label="Balance ( US dollar)")
      st.header(f"Current Balance: {veri.balance}$",divider="blue")
   if button23:
         veri.stock=True
   if veri.stock:
          stock()
                          
## stock prices input and select to position 

st.set_page_config(layout="wide",page_title="EFE BANK", page_icon="logo.jpg")
def finance(position):

    with position:
           with st.form("get_form"):          
              selection=st.multiselect("Select which stock you want to analyze",stock1)
              n=len(selection)
              button10=st.form_submit_button("Submit")
              if button10:
               for select in selection:
                  ask10=select.split(" ")[1] 
                  veri.liste.append(ask10)
              
               if  len(veri.liste[-n:])==n:
                with open(os.path.join(BASE_DIR, "stock.csv"),"a",encoding="utf-8") as file:
                  for code in veri.liste[-n:]:
                       file.write(f"{code},{veri.ıd}\n")
                if len(veri.liste[-n:])==n:
                  st.header("Stock Data", divider="blue")
                  df1=yf.download(veri.liste[-n:],period="5d", interval="1d",  auto_adjust=False, threads=False)
                  if not df1.empty:
                   st.badge(f"Stocks:{veri.liste[-n:]} " ,color="orange", icon="🪙")
                   st.dataframe(df1)                 
                  open1=df1[['Open','Adj Close']].stack(level=1).reset_index()
                  open1.rename(columns={'level_1':'Ticker'},inplace=True)
                  st.scatter_chart(data=open1, x='Adj Close', y='Open', color='Ticker')
## beggining screen 
if veri.step==0:
    im1,im2,im3=st.columns([1,1,1])
    with im1:
     st.image(str(yol/"image2.jpg"))
    with im2:
       st.image(str(yol/"image3.jpg"))
    with im3:
       st.image(str(yol/"image1.jpg"))
    button=st.button("Enter✨",width="stretch",type="primary")
    if button:
        veri.step=1
        st.rerun()
        time.sleep(2)
## form  page get users data
elif veri.step==1:
     st.write("EFE Bank🏦")
     with st.form("my_form"):
       veri.name=st.text_input("User Name")
       veri.ıd=st.text_input("Enter id")
       veri.password=st.text_input("Chose password\n(if already have account,enter 'Sign in🔐' button")
       button1=st.form_submit_button("Log in👤",type="primary")
       button2=st.form_submit_button("Sign in🔐", type="secondary")
     if veri.ıd and button1:
           with open (os.path.join(BASE_DIR, "user.csv"),"r") as file :
            lines=file.readlines()
            for line in lines:
             name,id,passwrd= line.rstrip().split(",")
           if veri.name in name or veri.ıd in id:
            start1=st.empty()
            start1.error("Name or ID is already taken !", icon=":material/thumb_up:" )
            time.sleep(5)
            start1.empty()
           with open(os.path.join(BASE_DIR, "user.csv"), "a", encoding="utf-8")as file:
               file.write(f"{veri.name},{veri.ıd},{veri.password}\n")
               file.close()
           user1=User(veri.name,veri.ıd,veri.password)
           veri.step=3
           st.rerun()
     elif button2 :
         veri.step=2
         time.sleep(2)
         lines=open(os.path.join(BASE_DIR, "user.csv"),"r", encoding="utf-8").readlines()
         @st.dialog("Sign İn")     
         def sign():
            with st.form("basic_form"):
               veri.ıd=st.text_input("ID")
               veri.password=st.text_input("Password")
               button4=st.form_submit_button("Sign in to your account")
       
            for line in lines:
              nm,ı,ps=line.rstrip().split(",")
              if veri.ıd == ı and veri.password==ps:
                with open(os.path.join(BASE_DIR, "user.csv"), "a", encoding="utf-8")as file:
                   file.write(f"{nm},{veri.ıd},{veri.password}\n")
                if button4:
                    veri.step=3
                    st.rerun()
              elif veri.ıd ==ı and veri.password!=ps:
                 st.empty()
                 st.error("Account couldnt found: There is no account about your ıd\n or password is wrong")
                 time.sleep(5)
                 st.empty()
         if veri.step==2:        
              sign() 
## main page
elif veri.step==3:
    st.title(f"Welcome {veri.name} to EFE Bank🏦")
    with st.sidebar:
      start=st.empty()
      start.success("Succesufly enter account")
      time.sleep(10)
      start.empty()
      st.logo(str(yol/"efe_bank_logo.jpg"), size="large" )
      st.write("Date:",date.today())
      button5=st.menu_button("Settings⚙️",options=["Log out", "❌ Delete account"])
      if button5=="❌ Delete account":
         @st.dialog
         def delet():
           st.write("if you wanted to delete your account enter 'Delete'")
           if st.button("Delete",type="primary"):
              with open(os.path.join(BASE_DIR, "user.csv"),"r", encoding="utf-8") as file:
                  lines=file.readlines()
                  for line in lines:
                      name,ıd,password=line.rstrip().split(",")
                      if ıd==veri.ıd:
                         df=pd.read_csv(os.path.join(BASE_DIR, "user.csv"), names=["Name","ID","Password"]) 
                         df=df[df['ID'] != veri.ıd]
                         df.to_csv(os.path.join(BASE_DIR, "user.csv"), index=False, header=False)
              veri.step=0
              st.rerun()
         delet()
      elif button5=="Log out":
         @st.dialog("Log Out")
         def out():
            st.write("İf you sure about log out click 'Log out' button.")
            b=st.button("Log out")
            if b:
             veri.step=0
             st.rerun()
         out()

      col1,col2=st.columns([1,5])
      with col1:
         st.image(str(yol/"insta.png"),width=30)
      with col2:
       st.link_button("My İnstagram","https://www.instagram.com/efe_.krks/" )
      page={"İnformations":[st.Page("about.py", title="About Us", icon="ℹ️"),
                            st.Page("accnt.py", title="Account information",icon =":material/person:"),
                            st.Page("past.py",title="Past Activites(Please Click)", icon="🤍")]}
      
      
      pg=st.navigation(page)
      pg.run()  
    
    left,mid, right= st.columns([0.3,0.4,0.3])
    finance(left)
    acnt_page(mid)
    lt.news(right)
                