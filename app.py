import spacy
from spacy.cli import download
import streamlit as st
from agents.plan_agent import PlanAgent
from tools.language_model_tool import LanguageModelTool
from tools.feedback_reflection import FeedbackReflection
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

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

# Function to process individual tasks with timeout
def process_task_with_timeout(task, timeout=10):
    try:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(plan_agent.process_task, task)
            return future.result(timeout=timeout)
    except Exception as e:
        return f"Task processing failed: {str(e)}"

# Main processing function
def process_query(user_query):
    # Plan tasks
    st.write("Planning tasks...")
    try:
        tasks = plan_agent.plan(user_query)
    except Exception as e:
        st.error(f"Error in task planning: {str(e)}")
        return [], {}

    st.write(f"Planned tasks: {tasks}")
    
    st.write("Processing tasks... This may take a moment.")

    # Use thread pool to process tasks in parallel with timeouts
    results = []
    for task in tasks:
        st.write(f"Processing task: {task}")
        result = process_task_with_timeout(task)
        st.write(f"Result: {result}")
        results.append(result)
    
    # Get feedback
    st.write("Generating feedback...")
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
        # Add a loading message
        with st.spinner("Processing your query..."):
            start_time = time.time()
            results, feedback = process_query(user_query)
            end_time = time.time()
            st.success(f"Query processed in {end_time - start_time:.2f} seconds")
        
        # Display results and feedback
        st.write("Results:")
        st.json(results)
        st.write("Feedback:")
        st.json(feedback)
    else:
        st.warning("Please enter a query.")
