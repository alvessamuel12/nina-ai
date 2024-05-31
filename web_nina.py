import streamlit as st
from llm import init_model
from modules.audio import listen, speak

# with st.sidebar:
name = 'Nina'
model = init_model(name)

st.title(f"💬 {name}")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Como posso lhe ajudar?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# if st.button("Record Audio", key="record_button"):
#     prompt = listen()
#     if prompt:
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         st.chat_message("user").write(prompt)
#         print(f'User input: {prompt}')
#         response = model.predict(input=prompt)
#         print(f'IA output: {response}')
        
#         st.session_state.messages.append({"role": "assistant", "content": response})
#         st.chat_message("assistant").write(response)   
#         speak(name, response)
# Inicializar o estado da sessão
if 'is_recording' not in st.session_state:
    st.session_state.is_recording = False
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Função para iniciar/parar gravação e transcrever o áudio
def toggle_recording():
    if st.session_state.is_recording:
        # Parar a gravação
        st.session_state.is_recording = False
        prompt = listen()
        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            print(f'User input: {prompt}')
            response = model.predict(input=prompt)
            print(f'IA output: {response}')
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)   
            speak(name, response)
    else:
        # Iniciar a gravação
        st.session_state.is_recording = True

# Botão para gravar áudio
if st.session_state.is_recording:
    if st.button("Stop Recording", key="stop_button"):
        toggle_recording()
else:
    if st.button("Record Audio", key="record_button"):
        toggle_recording()



if prompt := st.chat_input("Digite seu comando ou questão..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = model.predict(input=str(prompt))
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)