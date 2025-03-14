import streamlit as st
from scrape import scrape_website, extract_body_content, clean_body_content, split_dom_content

# main heading
st.title("AI Web Scraper")
st.write("Scrape any website and chat with the extracted data to get ONLY the most relevant data points for you.")
# insert a text input box
url = st.text_input("Enter a Website URL: ")

# when the button "Scrape Site" is clicked
if st.button("Scrape Site!"):
    st.write("Scraping the website...")
    st.write("A new window will open up, wait for it to close automatically.")
    st.write("Please wait for the website content to load below.")

    # get html page source
    result = scrape_website(url)

    # extract only the content in body tag
    body_content = extract_body_content(result)

    # clean the content to remove content in script and style tags
    cleaned_content = clean_body_content(body_content)

    # store content in streamlit session
    st.session_state.dom_content = cleaned_content

    # show content in collapsible streamlit expander
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse.")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content...")
           
            dom_chunks = split_dom_content(st.session_state.dom_content)


print("Done!")

