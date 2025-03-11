import streamlit as st

# main heading
st.title("AI Web Scraper")
# insert a text input box
url = st.text_input("Enter a Website URL: ")

# when the button "Scrape Site" is clicked
if st.button("Scrape Site!"):
    st.write("Scraping the website...")


