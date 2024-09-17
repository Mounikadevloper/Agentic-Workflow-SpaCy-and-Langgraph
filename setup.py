# setup.py
import spacy

def download_spacy_model():
    try:
        spacy.cli.download("en_core_web_sm")
    except Exception as e:
        print(f"Error downloading SpaCy model: {e}")

if __name__ == "__main__":
    download_spacy_model()
