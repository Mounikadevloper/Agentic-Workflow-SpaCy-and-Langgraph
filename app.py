# app.py
pip install spacy

import streamlit as st
import spacy  # Ensure spaCy is imported
from agents.plan_agent import PlanAgent
from tools.language_model_tool import LanguageModelTool
from tools.feedback_reflection import FeedbackReflection

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Initialize tools and agents
language_model_tool = LanguageModelTool()
feedback_reflection = FeedbackReflection()
plan_agent = PlanAgent(tools=[language_model_tool])

def process_query(user_query):
    # Plan tasks
    tasks = plan_agent.plan(user_query)
    
    # Process tasks
    results = []
    for task in tasks:
        result = plan_agent.process_task(task)
        results.append(result)
    
    # Provide feedback
    feedback = feedback_reflection.get_feedback(results)
    
    return results, feedback

# Streamlit app
st.title('Agentic Workflow Pipeline')

st.write("This application processes user queries using a pipeline of agents and tools.")

user_query = st.text_input("Enter your query:")

if st.button("Process Query"):
    if user_query:
        results, feedback = process_query(user_query)
        st.write("Results:")
        st.json(results)
        st.write("Feedback:")
        st.json(feedback)
    else:
        st.warning("Please enter a query.")
