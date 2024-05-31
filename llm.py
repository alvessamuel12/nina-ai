from typing import Literal
import os
import dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

dotenv.load_dotenv()



def init_model(model_name: Literal["Nora", "Max", "Nina"] = "Nina", max_tokens = 500):
    # Inicializando o modelo de linguagem
    llm = ChatGroq(temperature=0.2, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-70b-8192", max_tokens=max_tokens)

    # Inicializando a memória de conversação
    memory = ConversationBufferMemory(return_messages=True)
    gender = 'feminino' if model_name != 'Max' else 'masculino'
    memory.chat_memory.add_user_message(f"Seu nome é {model_name}, você é do gênero {gender}. Você é "+("um"if model_name == 'Max' else "uma")+" assistente pessoal inteligente, seu trabalho é facilitar a vida com informações. Seja agradável, "+("simpático" if model_name == 'Max' else "simpatica")+f", mas sem muitas brincadeiras. Responda com atenção as perguntas e seja o mais direto e objetivo possível e com o número máximo de caractéres de {max_tokens}. Sempre em português")
    memory.chat_memory.add_ai_message(f"Ok, meu nome é {model_name} e estou aqui para te ajudar")

    # Definindo a cadeia de conversação
    conversation = ConversationChain(
        llm=llm,
        verbose=True,
        memory=memory
    )
    return conversation

