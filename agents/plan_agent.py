# agents/plan_agent.py
import spacy

class PlanAgent:
    def __init__(self, tools):
        self.tools = tools
        self.nlp = spacy.load('en_core_web_sm')

    def plan(self, query):
        doc = self.nlp(query)
        # Simple implementation: split query into sentences or use some other logic
        tasks = [sent.text for sent in doc.sents]
        return tasks

    def process_task(self, task):
        # Find a tool to process the task
        for tool in self.tools:
            result = tool.apply_task(task)
            return result
