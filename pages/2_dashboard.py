import streamlit as st
from klassen import Studiengang
from datenverwaltung import Datenspeicherung, Nutzereingabe, Datenzugriff
import pandas as pd

aktueller_studiengang = Datenzugriff().studiengang_ausgeben()

st.markdown(f"Student: {aktueller_studiengang.student}")
st.header(f"📊 Dashboard für {aktueller_studiengang.bezeichnung}")



beste_note = [1,1,11,1]
col1, col2, col3, col4 = st.columns(4)

with col1.container(border=True,horizontal_alignment="center"):
    st.markdown('''
                :blue-background[**Durchschnitt**]
                ''')
    st.markdown(1)

with col2.container(border=True):
    st.markdown('''
                :blue-background[**ECTS-Punkte**]
                ''')
    st.markdown(2)

with col3.container(border=True):
    st.markdown('''
                :blue-background[**Beste Note**]
                ''')
    st.markdown(beste_note[1])
    st.markdown([beste_note[0], beste_note[2]])

with col4.container(border=True):
    st.markdown('''
                :blue-background[**Schlechteste Note**]
                ''')
    st.markdown(3)
    


st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.
            ''')

st.divider()

st.subheader("Neues Modul hinzufügen")


with st.form('modul_hinzufügen',clear_on_submit=True):
    modulname_wert = st.text_input("Modulname")
    modulnummer_wert = st.text_input("Modulnummer (Integer)")
    semester_wert = st.pills('Semester', [1,2,3,4,5,6], default=1)
    pruefungsart_wert = st.pills('Prüfungsart', ["Klausur", "Portfolio", "Workbook"], default="Klausur")
    ects_wert = st.pills("ECTS", [5,10], default=5)
    note_wert = st.segmented_control("Note", [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0], default=2.0)
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Hinzufügen")
    if submitted:
        st.write(modulname_wert, modulnummer_wert, semester_wert, pruefungsart_wert, ects_wert, note_wert)
        Nutzereingabe(modulname_wert, modulnummer_wert, semester_wert, pruefungsart_wert, ects_wert, note_wert)
        st.rerun()