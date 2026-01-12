import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Load and runs the langgraph agenticai application with Streamlit UI.
    this funciton initializes the ui, handles user input, configures the llm model,
    sets up the graph based on the selected usecase, and displays the output while
    implementing exception handling for robustness.
    
    """
    ## load ui
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("error : Failed to load user input from UI.")
        return
    
    user_message = st.chat_input("Enter your message: ")

    
    if user_message:
        try:
            obj_llm_config = GroqLLM(user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("Error : LLM model could not be initialized")
                return
            usecase  = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No usecase selected.")
                return
            # graph builder
            grap_builder=GraphBuilder(model)
            try:

                graph = grap_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_results_on_ui()
            except Exception as e:
                st.error(f"error : graph setup failed {e}")

        except Exception as e:
            st.error(f"Error : Graph setup failed {e}")
            return 

    