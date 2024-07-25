import streamlit as st
from streamlit_gsheets import GSheetsConnection

# ydata profiling
import pandas as pd
from ydata_profiling import ProfileReport

# report untuk streamlit
from streamlit_pandas_profiling import st_profile_report

# --- CONFIG
st.set_page_config(
    page_title = "Data Profiler Dashboard",
    page_icon = "📊",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

# --- JUDUL DASHBOARD
st.title('Data Profiler')
st.markdown("---")

# --- SIDEBAR
with st.sidebar:
    st.subheader("Promotion Data")
    st.markdown("---")

## --- Buat button
if st.sidebar.button("Start Profiling Data"):

    ## Read data
    conn = st.connection("gsheet", type=GSheetsConnection)

    df = conn.read(
        spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
        worksheet = st.secrets.gsheet_promotion["worksheet"]
    )

    ## Generate Report
    #---- progile report using ydata profiling
    pr = ProfileReport(df)

    # Display to streamlit
    st_profile_report(pr)

else:
    st.info("Click button in the left sidebar to start data profiling.")

