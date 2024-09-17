import spacy
import subprocess
import streamlit as st
import sys

# Function to ensure SpaCy and the model are available
def ensure_spacy_model():
    # Check if SpaCy is installed
    try:
        import spacy
    except ImportError:
        st.write("SpaCy not found. Installing SpaCy...")
        try:
            # Install SpaCy
            result = subprocess.run([sys.executable, "-m", "pip", "install", "spacy"], capture_output=True, text=True)
            st.write(f"Install output: {result.stdout}")
            st.write(f"Install error: {result.stderr}")
            import spacy  # Re-import after installation
        except Exception as e:
            st.error(f"An error occurred while installing SpaCy: {e}")
            return

    # Check if the SpaCy model is installed
    try:
        spacy.load('en_core_web_sm')
        st.write("SpaCy model is already installed and loaded.")
    except OSError:
        st.write("SpaCy model not found. Installing the model...")
        try:
            # Download the model
            result = subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], capture_output=True, text=True)
            st.write(f"Download output: {result.stdout}")
            st.write(f"Download error: {result.stderr}")
            
            spacy.load('en_core_web_sm')  # Load the model after download
            st.write("SpaCy model has been downloaded and loaded successfully.")
        except Exception as e:
            st.error(f"An error occurred while downloading the SpaCy model: {e}")

# Streamlit app interface
st.title('SpaCy Dependency Check')

# Ensure SpaCy and the model are available
ensure_spacy_model()

# Rest of your Streamlit app code
# Add additional functionality here
