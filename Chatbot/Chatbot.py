# from freeGPT import Client 
# while True:
#     prompt = input("input:")
#     try:
#         resp = Client.create_completion("gpt3", prompt)
#         print(f"hai: {resp}")
#     except Exception as e:  
#         print(f"hello: {e}")
 


from freeGPT import Client
import streamlit as st

st.title("Chat Bot (GPT-3.5)")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        full_response = Client.create_completion("gpt3", prompt)

    with st.chat_message("assistant"):
        st.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})



