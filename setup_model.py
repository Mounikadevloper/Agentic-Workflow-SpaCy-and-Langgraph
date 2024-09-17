import spacy

def install_spacy_model():
    try:
        spacy.cli.download("en_core_web_sm")
    except Exception as e:
        print(f"Error installing SpaCy model: {e}")

if __name__ == "__main__":
    install_spacy_model()
