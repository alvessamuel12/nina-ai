Nina AI
Nina é uma Inteligência Artificial avançada que permite conversas em tempo real por texto e voz, semelhante ao ChatGPT e Gemini. Ela pode ser utilizada via linha de comando, interface web utilizando Streamlit e uma interface gráfica nativa no sistema operacional.

Funcionalidades
Conversação via Texto: Interaja com Nina através de mensagens de texto.
Conversação via Voz: Utilize comandos de voz para conversar com Nina, com suporte para reconhecimento de fala e síntese de voz do Google.
Interface de Linha de Comando: Execute Nina diretamente do terminal para uma experiência simples e eficiente.
Interface Web: Utilize uma interface web interativa desenvolvida com Streamlit.
Interface Gráfica Nativa: Rode Nina como uma aplicação gráfica diretamente no seu sistema operacional.
Tecnologias Utilizadas
GROQ Cloud: Plataforma de computação em nuvem para acelerar operações de IA.
LangChain: Framework para construir aplicações de linguagem natural.
Python: Linguagem de programação principal utilizada no desenvolvimento de Nina.
Streamlit: Ferramenta para criar aplicações web interativas.
Google Speech Recognition: API para reconhecimento de fala.
Google Text-to-Speech: API para síntese de voz.
Requisitos
Python 3.8 ou superior
Conta e credenciais da Google Cloud para utilizar os serviços de Speech Recognition e Text-to-Speech.
Acesso ao GROQ Cloud (verifique a documentação oficial para configurações e credenciais)
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/alvessamuel12/nina-ai.git
cd nina-ai
Crie um ambiente virtual e instale as dependências:

bash
Copiar código
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
Configure as credenciais da Google Cloud:

Coloque o arquivo JSON de credenciais no diretório raiz do projeto.
Defina a variável de ambiente para o arquivo de credenciais:
bash
Copiar código
export GOOGLE_APPLICATION_CREDENTIALS="caminho/para/suas/credenciais.json"
Utilização
Linha de Comando
Execute o seguinte comando para iniciar Nina na linha de comando:

bash
Copiar código
python cli_nina.py
Interface Web (Streamlit)
Para iniciar a interface web, execute:

bash
Copiar código
streamlit run web_nina.py
Acesse http://localhost:8501 no seu navegador.

Interface Gráfica Nativa
Para utilizar a interface gráfica nativa, execute:

bash
Copiar código
python gui_nina.py
Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/sua-feature).
Commit suas mudanças (git commit -m 'Adicionei uma nova feature').
Faça o push para a branch (git push origin feature/sua-feature).
Abra um Pull Request.
Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Para mais informações ou suporte, entre em contato com alvessamuel12@outlook.com.

Nina AI - Inteligência Artificial para conversas por texto e voz, onde e como você preferir.
