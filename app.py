import spacy
import subprocess
import streamlit as st
import sys
import os

def ensure_spacy_model():
    # Function to check if SpaCy is installed and load the model
    def install_spacy_and_model():
        st.write("Attempting to install SpaCy and download the model...")

        try:
            # Install SpaCy
            result = subprocess.run([sys.executable, "-m", "pip", "install", "spacy"], capture_output=True, text=True)
            if result.returncode != 0:
                st.error(f"Error installing SpaCy: {result.stderr}")
                return

            # Download the model
            result = subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], capture_output=True, text=True)
            if result.returncode != 0:
                st.error(f"Error downloading SpaCy model: {result.stderr}")
                return

            # Verify installation
            try:
                import spacy
                spacy.load('en_core_web_sm')
                st.write("SpaCy and the model have been installed and downloaded successfully.")
            except Exception as e:
                st.error(f"An error occurred while loading SpaCy model: {e}")

        except Exception as e:
            st.error(f"An error occurred during installation: {e}")

    # Check if SpaCy model is already installed
    try:
        spacy.load('en_core_web_sm')
        st.write("SpaCy model is already installed and loaded.")
    except OSError as e:
        st.write("SpaCy model not found. Installing...")
        install_spacy_and_model()
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# Streamlit app interface
st.title('SpaCy Dependency Check')

# Ensure SpaCy and the model are available
ensure_spacy_model()

# Rest of your Streamlit app code
# Add additional functionality here
