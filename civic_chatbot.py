import streamlit as st
import google.generativeai as genai

# Access the Gemini API key from Streamlit secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # Select the Gemini model
    model = genai.GenerativeModel('gemini-2.0-flash')
except KeyError:
    st.error("The Google API key was not found in Streamlit secrets. Please ensure you have a `.streamlit/secrets.toml` file with the key `GOOGLE_API_KEY`.")
    st.stop()

def get_civic_sense_response(query):
    prompt = f"""Answer the following question about civic duties in India by providing a concise response that includes:
    - A Clear and Simple Explanation of the duty (maximum 2 sentences).
    - Real-Life Examples relevant to India (use bullet points, maximum 2 examples).
    - An explanation Addressing Hesitations and Misconceptions (maximum 2 sentences, highlight the core reasons).
    - Information that provides Empowerment through Knowledge (maximum 2 sentences, highlight the key takeaway in bold).
    - Positive Reinforcement emphasizing the benefits (use bullet points, highlight the main benefit in bold).

    Question: {query}"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
st.title("Civic Sense Chatbot")
st.markdown("**Civic sense is the basic social etiquette and responsibility we all need to be good citizens, including respecting laws, public property, and the rights of others.**")

user_query = st.text_input("Ask your question about civic duties here:")

if st.button("Ask"):
    if user_query:
        st.write("Generating response...")
        chatbot_response = get_civic_sense_response(user_query)
        st.subheader("Chatbot's Response:")
        st.write(chatbot_response)
    else:
        st.warning("Please enter your question.")