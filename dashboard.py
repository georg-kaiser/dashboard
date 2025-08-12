import streamlit as st
from datenverwaltung import Nutzereingabe, Datenzugriff
import pandas as pd

#Der akutelle Studiengang wird abgerufen
aktueller_studiengang = Datenzugriff().studiengang_ausgeben()

#Name des Studenten anzeigen
st.markdown(f"Student: {aktueller_studiengang.student}")
#Überschrift inkl. Studiengang-Bezeichnung
st.header(f"📊 Dashboard für {aktueller_studiengang.bezeichnung}")



#Für die Übersichtlichkeit werden vier Spalten erstellt und im Anschluss mit Daten gefüllt
col1, col2, col3, col4 = st.columns(4)

# Spalte 1: enthält den Notendurchschnitt und vergleicht diesen, ob er besser oder schlechter als 2.0 ist 
with col1.container(border=True, height=180):
    st.markdown(''':blue-background[**Durchschnitt**]''') 
    #besser als 2.0
    if aktueller_studiengang.notenduchschnitt_gesamt < 2.0: 
        st.metric(
            label="",
            value=f"⌀ {aktueller_studiengang.notenduchschnitt_gesamt}",
            delta="besser als 2.0"
            )
    #schlechter als 2.0
    elif aktueller_studiengang.notenduchschnitt_gesamt > 2.0:
        st.metric(
            label="",
            value=f"⌀ {aktueller_studiengang.notenduchschnitt_gesamt}",
            delta="-schlechter als 2.0" #Minus am Anfang vom String zeigt Streamlit, dass die Farbe sich auf rot änderen soll
            ) 
    #gleich 2.0
    else:   
        st.metric(label="",
            value=f"⌀ {aktueller_studiengang.notenduchschnitt_gesamt}",
            delta="genau 2.0",
            delta_color="off"
                  )

# Spalte 2: enthält die Gesamt-ECTS
with col2.container(border=True, height=180):
    st.markdown(''':blue-background[**ECTS-Punkte**]''')
    st.metric(
        label="",
        value=aktueller_studiengang.ects_gesamt
              )

# Spalte 3: enthält die beste Note inkl. Modulname und Prüfungsart
with col3.container(border=True, height=180):
    st.markdown(''':blue-background[**Beste Note**]''')
    st.metric(
        label=aktueller_studiengang.beste_pruefungsart,
        value=aktueller_studiengang.beste_note,
        delta=aktueller_studiengang.bestes_modul
              )

# Spalte 4: enthält die schlechteste Note inkl. Modulname und Prüfungsart
with col4.container(border=True, height=180):
    st.markdown(''':blue-background[**Schlechteste Note**]''')
    st.metric(
        label=aktueller_studiengang.schlechteste_pruefungsart,
        value=aktueller_studiengang.schlechteste_note,
        delta=f"-{aktueller_studiengang.schlechtestes_modul}" #Minus am Anfang vom String zeigt Streamlit, dass die Farbe sich auf rot änderen soll
              )  
    


#Trennstrich
st.divider()

#Unterüberschrift
st.subheader("ECTS pro Semester")
#Erstellt einen DataFrame mit den ECTS der einzelnen Semester
df = pd.DataFrame(Datenzugriff().ects_semeseter_ausgeben())
#Gibt den oben erstellten DataFrame als Säulendiagramm aus
st.bar_chart(data=df, x="Semester", y="ECTS")

#Trennstrich
st.divider()



#Unterüberschrift
st.subheader("Neues Modul hinzufügen")

#Erstellt ein Formular, dass den Nutzer auffordert, alle Daten einzugeben, um ein neues Modul hinzuzufügen
#Folgende Daten werden verlangt: Modulname, Modulnummer, Semesternummer, Pruefungsart, ECTS und Note
with st.form('modul_hinzufügen',clear_on_submit=True):
    modulname_wert = st.text_input("Modulname (Pflichtfeld)")
    modulnummer_wert = st.text_input("Modulnummer (Pflichtfeld)")
    semester_wert = st.pills('Semester', [1,2,3,4,5,6], default=1) #Standart: Semester 1
    pruefungsart_wert = st.pills('Prüfungsart', ["Klausur", "Portfolio", "Workbook"], default="Klausur") #Standart: Klausur
    ects_wert = st.pills("ECTS", [5,10], default=5) #Standart: 5 ECTS
    note_wert = st.segmented_control("Note", [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0], default=2.0) #Standart: Note 2.0
    
    #Erstellt einen Knopf um das Formular einzureichen
    submitted = st.form_submit_button("Hinzufügen")
    if submitted:
        #Falls die Felder ohne Standartwert nicht ausgefüllt werden, wird dem Nutzer eine Fehlermeldung angezeigt
        if not modulname_wert or not modulnummer_wert:
            st.error("Bitte Pflichtfelder ausfüllen!")
        #Wenn alles korrekt ausgefüllt wurde, werden die Daten an die Nutzereingabe-Klasse weitergeben
        else:
            Nutzereingabe(modulname_wert, modulnummer_wert, semester_wert, pruefungsart_wert, ects_wert, note_wert)
            #Daraufhin wird die Website aktualisiert, damit das neue Modul mit angezeigt wird
            st.rerun()