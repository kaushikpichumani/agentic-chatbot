from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    
    Return the list of tools to be used for chatbot


    """
    tools =TavilySearch(max_results = 2)
    return [tools]

def create_tool_node(tools):
    """ 
    
    create and return a tool nodel for the graph
    
    """

    return ToolNode(tools=tools)