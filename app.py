import spacy
import subprocess
import streamlit as st
import sys
import spacy
spacy.cli.download("en-core-web-sm")


def ensure_spacy_model():
    try:
        spacy.load('en_core_web_sm')
        st.write("SpaCy model is already installed and loaded.")
    except OSError:
        st.write("SpaCy model not found. Installing SpaCy and downloading the model...")
        try:
            # Install SpaCy
            result = subprocess.run([sys.executable, "-m", "pip", "install", "spacy"], capture_output=True, text=True)
            st.write(f"Install output: {result.stdout}")
            st.write(f"Install error: {result.stderr}")
            
            # Download the model
            result = subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], capture_output=True, text=True)
            st.write(f"Download output: {result.stdout}")
            st.write(f"Download error: {result.stderr}")

            spacy.load('en_core_web_sm')
            st.write("SpaCy and the model have been installed and downloaded successfully.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Streamlit app interface
st.title('SpaCy Dependency Check')

# Ensure SpaCy and the model are available
ensure_spacy_model()

# Rest of your Streamlit app code
