import streamlit as st

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client with your key
client = OpenAI(api_key=api_key)

# Now you can use the client to make API calls
response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": "enhance the prompt"}])

st.set_page_config(page_title="Prompt Enhancer", page_icon="📝")
st.title("📝 Prompt Engineer — General Prompt Enhancer")


st.caption("Demo Mode - Learn how to structure better prompts!")


st.subheader("Enter Context, Constraint, Structure, Checkpoint, Review (CC-SC-R)")
context = st.text_input("Context", value="Detailed context of the task")
constraint = st.text_area("constraint", value="Mention all constraints to keep in mind")
structure = st.text_area("structure", value="Define the structure of the output desired")
checkpoint = st.text_area("checkpoint", value="Define the checks you want to put in the system")
review = st.text_area("review", value="Reviews to be built into the system")


st.subheader("Paste your rough prompt")


draft = st.text_area("Your draft prompt:", height=140)


if st.button("Enhance Prompt"):
    if not draft.strip():




        st.warning("Please enter a draft prompt.")


    else:
        # Demo output - shows structured approach
        instruction = (
            "Generate an enhanced, structured prompt using RCT.\n"
            "1) Improve clarity and completeness\n"
            "2) Ask ONE clarifying question\n"
            "3) Specify output format (3 bullets, ≤12 words each)\n"
        )
        demo_output = (
            f"CONTEXT: {context}\n"
            f"CONSTRAINT: {constraint}\n"
            f"STRUCTURE: {structure}\n"
            f"CHECKPOINT: {checkpoint}\n"
            f"REVIEW: {review}\n\n"
            f"USER DRAFT:\n{draft}\n\n"
            "OUTPUT FORMAT:\n- 3 concise bullets\n- 1 clarifying question"
        )
        
        st.success("Enhanced Prompt (Demo Mode)")
        st.code(instruction + "\n" + demo_output, language="markdown")
        
        st.info("💡 This is demo mode showing the RCT structure. In live mode, AI would generate the actual enhanced prompt!")