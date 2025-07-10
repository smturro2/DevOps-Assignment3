import streamlit as st
from backend import get_available_countries, get_country_data, format_number


countries = get_available_countries()

st.title("Country Getter GUI")
with st.form("my_form"):
    st.write("Select Countries to Pull data from")
    selected_countries = st.multiselect("Countries", countries, default=countries[:2])
    format_data = st.checkbox("Format Data", value=True)
    submit_button = st.form_submit_button("Submit")
    
if submit_button:
    st.header("Data for Countries:")
    data = get_country_data(selected_countries)
    if format_data:
        data = data.applymap(format_number)
    st.dataframe(data)