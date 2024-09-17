from setuptools import setup

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
)
