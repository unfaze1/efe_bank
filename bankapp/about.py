import streamlit as st
veri=st.session_state

st.write("EFE Bank is a digital bank system that allows users to manage their finances online.\n Our mission is to provide a seamless banking experience with top-notch security and user-friendly features.")
file=open("video1.mp4", "rb")
read=file.read()
st.video(read,alt="presentation")
st.subheader(f"Thank for watching {veri.name} ")