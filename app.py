import streamlit as st
import spacy
from agents.plan_agent import PlanAgent
from tools.language_model_tool import LanguageModelTool
from tools.feedback_reflection import FeedbackReflection

def load_spacy_model(model_name='en_core_web_sm'):
    try:
        return spacy.load(model_name)
    except OSError:
        import spacy.cli
        spacy.cli.download(model_name)
        return spacy.load(model_name)
    except Exception as e:
        st.error(f"An error occurred while loading the SpaCy model: {e}")
        return None

nlp = load_spacy_model()

if nlp is None:
    st.error("SpaCy model could not be loaded. Please check the logs.")
else:
    # Initialize tools and agents
    language_model_tool = LanguageModelTool()
    feedback_reflection = FeedbackReflection()
    plan_agent = PlanAgent(tools=[language_model_tool])

    def process_query(user_query):
        tasks = plan_agent.plan(user_query)
        results = []
        for task in tasks:
            result = plan_agent.process_task(task)
            results.append(result)
        feedback = feedback_reflection.get_feedback(results)
        return results, feedback

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
