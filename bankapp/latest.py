import yfinance as yf
import streamlit as st
from pathlib import Path
yol=Path(__file__).resolve().parent

class late:
 def news(position):
  with position:
   veri=st.session_state
   liste1=["apple.png","nvi.png","jpmorgan.png","amazon.png","meta1.png","tesla.png"]
   liste=["AAPL","NVDA","JPM","AMZ","META","TSLA"]
   metrics=[["Latest News","APPLE"],["Latest News","NVIDIA"],["Latest News","JP Morgan"],["Latest News","Amazon"],["Latest News","META"],["Latest News","TESLA"]]
   grid=st.columns(6)
   st.header("⚡Most promintal companies daily news🌍",divider="blue")
   for image,grids,stock,metric in zip(liste1,grid,liste,metrics): 
    ticker=yf.Ticker(stock)
    info=ticker.info
    news=ticker.news
    for new in news:
      content=new.get("content",new)
      title=content.get("title")
      summary=content.get("summary")
      article=content.get("canonicalUrl",{}).get("url") or content.get("link")
    with grids:
     with st.popover("Title"):
      st.write(f"{title}")
     st.image(str(yol/image),width=200)  
     grids.metric(metric[1],stock,border=True)
     st.link_button(f"See Latest news...", article,type="primary")
  


