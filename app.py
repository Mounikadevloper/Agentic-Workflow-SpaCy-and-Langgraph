import spacy
from spacy.cli import download
import streamlit as st
from agents.plan_agent import PlanAgent
from tools.language_model_tool import LanguageModelTool
from tools.feedback_reflection import FeedbackReflection

# Load SpaCy model (with error handling to ensure the model is downloaded)
@st.cache_resource
def load_spacy_model():
    try:
        return spacy.load('en_core_web_sm')
    except OSError:
        download('en_core_web_sm')
        return spacy.load('en_core_web_sm')

nlp = load_spacy_model()

# Cache the initialization of agents and tools
@st.cache_resource
def load_plan_agent():
    language_model_tool = LanguageModelTool()
    feedback_reflection = FeedbackReflection()
    return PlanAgent(tools=[language_model_tool]), feedback_reflection

plan_agent, feedback_reflection = load_plan_agent()

def process_query(user_query):
    # Debugging statements for each step
    st.write("Planning tasks...")
    tasks = plan_agent.plan(user_query)
    st.write(f"Planned tasks: {tasks}")
    
    st.write("Processing tasks...")
    results = []
    for task in tasks:
        st.write(f"Processing task: {task}")
        result = plan_agent.process_task(task)
        st.write(f"Result: {result}")
        results.append(result)
    
    st.write("Getting feedback...")
    feedback = feedback_reflection.get_feedback(results)
    
    return results, feedback

# Streamlit app interface
st.title('Agentic Workflow Pipeline')

st.write("This application processes user queries using a pipeline of agents and tools.")

# User input
user_query = st.text_input("Enter your query:")

# Process the query on button click
if st.button("Process Query"):
    if user_query:
        results, feedback = process_query(user_query)
        st.write("Results:")
        st.json(results)
        st.write("Feedback:")
        st.json(feedback)
    else:
        st.warning("Please enter a query.")
