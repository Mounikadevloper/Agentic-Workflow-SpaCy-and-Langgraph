from setuptools import setup
import subprocess
import sys

def install_spacy_model():
    subprocess.check_call([sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'])

# Run the function to install the SpaCy model
install_spacy_model()

setup(
    name='agentic-workflow',
    version='0.1',
    packages=['agents', 'tools'],
    install_requires=[
        'streamlit',
        'spacy',
        'transformers',
        # Add other dependencies as needed
    ],
    # Add other setup parameters if needed
)
