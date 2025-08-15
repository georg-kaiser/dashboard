import streamlit as st
from klassen import Studiengang
from datenverwaltung import Datenspeicherung



#Überschrift
st.header("Bitte Studiengang angeben")  


#Erstellt ein Formular, in dem der Nutzer seinen Studiengang und seinen Namen angibt
with st.form("Studiengang"):    
    neue_bezeichnung = st.text_input("Studiengang Bezeichnung")
    neuer_student = st.text_input("Name Student")

    #Um das Formular einzureichen, gibt es eine Knopf
    submitted = st.form_submit_button("Studiengang festlegen")  

    #Wenn der Knopf gedrückt wird, wird ein Studiengang-Objekt erstellt und abgespeichert
    if submitted:   
        neuer_studiengang = Studiengang(bezeichnung=neue_bezeichnung, student=neuer_student, semester_liste=[1,2,3,4,5,6])
        Datenspeicherung(neuer_studiengang)
        #Danach wird der nutzer an das Dashbaord weitergeleitet
        st.switch_page("dashboard.py") 
