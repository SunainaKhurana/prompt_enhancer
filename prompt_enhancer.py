import streamlit as st
from openai import OpenAI


# Function to enhance the prompt
def enhance_prompt(api_key, context, constraint, structure, checkpoint, review):
    instruction = (
        "Given the following Context, Constraint, Structure, Checkpoint and Review, generate an enhanced, structured prompt. "
        "The prompt must: "
        "1. Improve clarity and completeness. "
        "2. Request GPT to clarify assumptions before responding. "
        "3. Specify an expected output format (e.g., bullet points, JSON, structured text)."
    )

    user_input = f"Context: {context}\n Constraint: {constraint}\n Structure: {structure}\n Checkpoint: {checkpoint}\n Review: {review}"
    final_prompt = f"{instruction}\n\n{user_input}"

    try:
        # Initialize client with the API key
        client = OpenAI(api_key=api_key)

        # Create a chat completion with the updated API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": final_prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


# Streamlit UI
def main():
    st.title("AI Prompt Enhancer")
    st.write("Improve and structure your prompts for better AI responses.")

    # Sidebar for API key input
    st.sidebar.header("Settings")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

    context = st.text_input("context", "")
    constraint = st.text_area("constraint", "")
    structure = st.text_area("structure", "")
    checkpoint = st.text_area("checkpoint", "")
    review = st.text_area("review", "")


    if st.button("Enhance Prompt"):
        if not api_key:
            st.warning("Please enter your OpenAI API key in the sidebar.")
        elif context and constraint and structure and checkpoint and review:
            with st.spinner("Enhancing your prompt..."):
                enhanced_prompt = enhance_prompt(api_key, context, constraint, structure, checkpoint, review)

                if enhanced_prompt.startswith("Error:"):
                    st.error(enhanced_prompt)
                else:
                    st.subheader("Enhanced Prompt:")
                    st.code(enhanced_prompt, language="markdown")
        else:
            st.warning("Please fill in all fields before generating.")


if __name__ == "__main__":
    main()

