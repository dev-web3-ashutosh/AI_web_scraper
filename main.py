import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content


# main heading
st.title("AI Web Scraper")
# insert a text input box
url = st.text_input("Enter a Website URL: ")

# when the button "Scrape Site" is clicked
if st.button("Scrape Site!"):
    st.write("Scraping the website... A new window will open up, wait for it to close automatically.")
    result = scrape_website(url)
    print(result)

