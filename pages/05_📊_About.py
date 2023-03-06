import streamlit as st
import pandas as pd
import datetime
from modules.formater import Title

# Title page and footer
title = "📊 About"
Title().page_config(title)

st.markdown("## 📊 About")
st.markdown("### 👨🏼‍💻 Goal")
st.markdown("""
Open-sourcing job requirements for aspiring data analysts is necessary for data Enthusiast to focus more efficiently on what skills they need to learn for their future job. This dashboard is only the beginning of that journey. \n 
""")

st.markdown("### 🤖 Resources")
st.markdown(f"""
Thanks to [SerpApi](https://serpapi.com/) for providing the resources to pull this data! 🙌🏼 """)

st.markdown("### 📈 Data")
st.markdown(f"""
Data is collected daily from Google job postings search results; specifically, [searching for Data Analyst in the United States](https://serpapi.com/playground?engine=google_jobs&q=Data+Analyst&location=United+States&gl=us&hl=en). As the project grows, we'll expand to other regions and disciplines. More info in links below.👇🏼 \n
""")


