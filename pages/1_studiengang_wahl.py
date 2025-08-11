import streamlit as st
from klassen import Studiengang
from datenverwaltung import Datenspeicherung

col1, col2, col3 = st.columns([1,1,1])

with col2.container(horizontal_alignment="center"):
    st.header("Bitte Studiengang angeben")
    with st.form("Studiengang"):
        neue_bezeichnung = st.text_input("Studiengang Bezeichnung")
        neuer_student = st.text_input("Name Studnet")

            # Every form must have a submit button.
        submitted = st.form_submit_button("Studiengang festlegen")
        if submitted:
            st.write("Studiengang gewählt!")
            neuer_studiengang = Studiengang(bezeichnung=neue_bezeichnung, student=neuer_student, semester_liste=[])
            Datenspeicherung(neuer_studiengang)
            st.switch_page("pages/2_dashboard.py")

