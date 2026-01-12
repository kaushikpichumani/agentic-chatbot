
from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic chatbot login implemintation
    
    """

    def __init__(self,model):
        self.llm=model

    def process(self,state:State)-> dict:
        """
        process the input state and generate a chatbot response
        """

        return {"messages":self.llm.invoke(state["messages"])}