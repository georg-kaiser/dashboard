import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Dashboard",
    page_icon="📊",
                   )

pg = st.navigation([
        st.Page("pages/1_studiengang_wahl.py", title="Studiengang"),
        st.Page("pages/2_dashboard.py", title="Dashboard"),
    ], position="hidden")
pg.run()
