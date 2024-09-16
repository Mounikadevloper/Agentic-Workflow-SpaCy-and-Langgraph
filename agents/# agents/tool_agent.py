# agents/tool_agent.py
class ToolAgent:
    def __init__(self, tools):
        self.tools = tools

    def execute_task(self, task):
        for tool in self.tools:
            result = tool.apply_task(task)
            return result
