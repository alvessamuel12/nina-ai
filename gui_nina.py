import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from llm import init_model
from modules.audio import listen, speak

class ChatBubble(QFrame):
    def __init__(self, text, role="user"):
        super().__init__()
        self.initUI(text, role)

    def initUI(self, text, role):
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setWordWrap(True)
        label.setFont(QFont("Arial", 14))
        
        if role == "user":
            label.setStyleSheet("background-color: #DCF8C6; padding: 10px; border-radius: 10px;")
            layout.setAlignment(Qt.AlignRight)
        else:
            label.setStyleSheet("background-color: #FFFFFF; padding: 10px; border-radius: 10px;")
            layout.setAlignment(Qt.AlignLeft)
        
        layout.addWidget(label)
        self.setLayout(layout)
        self.setMaximumWidth(400)

class ChatWindow(QMainWindow):
    def __init__(self, name, model):
        super().__init__()
        self.name = name
        self.model = model
        self.initUI()
        self.messages = [{"role": "assistant", "content": "Como posso lhe ajudar?"}]
        self.update_display()

    def initUI(self):
        self.setWindowTitle(f'Assistente Pessoal - {self.name}')
        self.setGeometry(200, 200, 400, 600)

        # Layout principal
        main_layout = QVBoxLayout()

        # Área de exibição de mensagens
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_layout.addStretch(1)
        self.chat_container.setLayout(self.chat_layout)
        self.scroll_area.setWidget(self.chat_container)

        main_layout.addWidget(self.scroll_area)

        # Campo de entrada de texto
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Digite seu comando ou questão...")
        self.text_input.returnPressed.connect(self.send_message)

        # Botão de enviar mensagem
        send_button = QPushButton('Enviar')
        send_button.clicked.connect(self.send_message)

        # Botão de gravação de áudio
        record_button = QPushButton('Record Audio')
        record_button.clicked.connect(self.record_audio)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(send_button)
        input_layout.addWidget(record_button)

        main_layout.addLayout(input_layout)

        # Container principal
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def update_display(self):
        for i in reversed(range(self.chat_layout.count() - 1)):
            self.chat_layout.itemAt(i).widget().setParent(None)

        for msg in self.messages:
            role = "Você" if msg['role'] == 'user' else self.name
            bubble = ChatBubble(msg['content'], role)
            self.chat_layout.insertWidget(self.chat_layout.count() - 1, bubble)
        
        self.chat_container.adjustSize()
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def send_message(self):
        prompt = self.text_input.text()
        if prompt:
            self.messages.append({"role": "user", "content": prompt})
            self.update_display()
            response = self.predict_response(prompt)
            self.messages.append({"role": "assistant", "content": response})
            self.update_display()
            self.text_input.clear()

    def record_audio(self):
        prompt = listen()
        if prompt:
            self.messages.append({"role": "user", "content": prompt})
            self.update_display()
            response = self.predict_response(prompt)
            self.messages.append({"role": "assistant", "content": response})
            self.update_display()
            speak(self.name, response)

    def predict_response(self, prompt):
        response = self.model.predict(input=prompt)
        return response

if __name__ == '__main__':
    name = 'Nina'
    model = init_model(name)

    app = QApplication(sys.argv)
    window = ChatWindow(name, model)
    window.show()
    sys.exit(app.exec_())
