import streamlit as st
import os



#Konfigueiert die Website
st.set_page_config(
    layout="centered",
    page_title="Dashboard",
    page_icon="📊"
    )

#Überprüft, ob bereits ein Studiengang exisitert oder ob der Nutzer das Programm zum ersten Mal ausführt.
if os.path.exists('studiengang.json'):
    pg = st.navigation([
        st.Page("dashboard.py"), #Studiengang existiert bereits, Nutzer wird direkt ans Dashboard weitergeleitet
        st.Page("studiengang_wahl.py"),
        ],
        position="hidden"
        )
else:
    pg = st.navigation([
        st.Page("studiengang_wahl.py"), #Studiengang existiert nicht, Nutzer wird erst an Studiengang-Wahl weitergeleitet
        st.Page("dashboard.py")
        ],
        position="hidden"
        )

#Führt die Webseite aus
pg.run() 
