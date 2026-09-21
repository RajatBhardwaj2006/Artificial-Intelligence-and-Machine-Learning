import streamlit as st
from analyzer import youtube_agent

st.set_page_config(
    page_title="Youtube Video analyzer", 
    layout="centered"
)

st.title("Youtube Video Analyzer.")

def get_agent():
    return youtube_agent()

agent = get_agent()

# input space

video_url = st.text_input("Enter Video URL: ")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing Video..."):
        response = agent.run(
            f"Analyze this Video: {video_url}"
        )
    st.markdown("Report of Video: ")
    st.markdown(response.content)    