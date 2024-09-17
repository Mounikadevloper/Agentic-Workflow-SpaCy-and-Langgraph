import spacy
import subprocess
import streamlit as st
import sys
import os

def ensure_spacy_model():
    # Function to check if SpaCy is installed and load the model
    def install_spacy_and_model():
        st.write("Installing SpaCy and downloading the model...")
        try:
            # Install SpaCy
            result = subprocess.run([sys.executable, "-m", "pip", "install", "--user", "spacy"], capture_output=True, text=True)
            st.write(f"Install output: {result.stdout}")
            st.write(f"Install error: {result.stderr}")
            
            # Download the model
            result = subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], capture_output=True, text=True)
            st.write(f"Download output: {result.stdout}")
            st.write(f"Download error: {result.stderr}")

            # Reload SpaCy after installation
            import spacy
            spacy.load('en_core_web_sm')
            st.write("SpaCy and the model have been installed and downloaded successfully.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    try:
        spacy.load('en_core_web_sm')
        st.write("SpaCy model is already installed and loaded.")
    except OSError:
        install_spacy_and_model()

# Streamlit app interface
st.title('SpaCy Dependency Check')

# Ensure SpaCy and the model are available
ensure_spacy_model()

# Rest of your Streamlit app code
# Add additional functionality here
