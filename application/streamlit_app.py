import streamlit as st
import io   
from utils.config_loader import ConfigLoader
from models.summarizer_model import Summarization
from models.preprocessing import PreProcessing
from custom_logger.custom_logging import CustomLogger


logger = CustomLogger.get_logger("StreamlitAPP")

def run_streamlit_app():
    st.title("Text Summarization")
    st.write("Enter Text Below To Generate A Summary Using The Pegasus Model.")

    config = ConfigLoader.load_config("config.yaml")
    if config is None:
        st.error("Failed to load configuration. Please check config.yaml.")
        logger.error("Failed to load configuration.")
    else:
        summarize = Summarization()
        summarize.load_model()
    

    user_input = st.text_area("Enter Text to Summarize", height = 200)

    if st.button("Summarize"):
        if user_input.strip():
            preprocessing_text = PreProcessing.preprocessing_func(user_input)

            summary = summarize.summarize_text(preprocessing_text)

            if summary:
                st.subheader("Summary:")
                st.write(summary)
                logger.info("Summary generated successfully.")

                text_io = io.StringIO()
                text_io.write(summary)
                text_io.seek(0)

                st.download_button(
                    label = "Download Summary as Text File",
                    data = text_io.getvalue(),
                    file_name = "summary.txt",
                    mime="text/plain"
                )
            else:
                st.error("Failed to generate summary.")
                logger.error("Summarization failed.")
        else:
            st.warning("Please enter some text to summarize.")  