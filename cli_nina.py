from llm import init_model
from modules.audio import speak, prompt_listen
import pprint

model_name = 'Nina'
model = init_model(model_name)
saudacao = 'Olá eu sou ' + (f'a {model_name}' if model_name != 'Max' else f'o {model_name}')+', como posso lhe auxiliar hoje?'
speak(voice_name=model_name, text=saudacao)
# Loop de interação contínua
while True:
    # Capturando a entrada do usuário
    user_input = prompt_listen()

    # Prevendo a resposta do modelo
    response = model.predict(input=user_input)
    print(response)
    # Falando a resposta
    speak(voice_name=model_name, text=response)
