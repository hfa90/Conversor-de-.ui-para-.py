
# Fornece acesso a variáveis e funções do sistema.
import sys          
# Permite interação com o sistema operacional (arquivos, diretórios, etc.).
import os           
# Importa classes do PyQt5 para criar a interface gráfica.
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton, QLineEdit, QVBoxLayout, QWidget

# Definição da classe principal para a janela:
class ConverterUI(QMainWindow):
    # Método construtor:
    def __init__(self):
        # Chama o construtor da classe pai (QMainWindow).
        super().__init__() 
        # Inicializa os elementos da interface da janela.
        self.initUI()   

    # Método de inicialização da interface:
    def initUI(self):
        # Define o título da janela.
        self.setWindowTitle("Hayden - UI / PY")

        # Cria um layout vertical para organizar os elementos.
        layout = QVBoxLayout() 

        # Cria um campo de texto para exibir/inserir o caminho do arquivo .ui.
        self.uiFilePath = QLineEdit(self)   
        # Define o texto de placeholder (dica) para o campo.
        self.uiFilePath.setPlaceholderText("Selecione o arquivo .ui")  
        # Adiciona o campo de texto ao layout.
        layout.addWidget(self.uiFilePath)  

        # Cria um botão para selecionar o arquivo .ui.
        self.selectFileButton = QPushButton("Selecione o Arquivo", self)  
        # Conecta o evento de clique do botão à função 'select_file'.
        self.selectFileButton.clicked.connect(self.select_file)  
        # Adiciona o botão de seleção ao layout.
        layout.addWidget(self.selectFileButton)  

        # Cria um botão para converter o arquivo .ui para .py.
        self.convertButton = QPushButton("Clique Aqui para Converter para Py", self)  
        # Conecta o evento de clique do botão à função 'convert_file'.
        self.convertButton.clicked.connect(self.convert_file)  
        # Adiciona o botão de conversão ao layout.
        layout.addWidget(self.convertButton)

        # Cria um widget para conter o layout.
        container = QWidget()   
        # Define o layout para o widget container.
        container.setLayout(layout)   
        # Define o widget container como o widget central da janela.
        self.setCentralWidget(container)    

    # Método para selecionar o arquivo .ui:
    def select_file(self):
        # Opções para o diálogo de seleção de arquivo.
        options = QFileDialog.Options()    
        # Define a opção de leitura como padrão.
        options |= QFileDialog.ReadOnly    
        # Abre o diálogo de seleção e armazena o nome do arquivo selecionado e o filtro.
        fileName, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo .ui", "", "Arquivos UI (*.ui);;Todos os arquivos (*)", options=options) 
        # Se um arquivo foi selecionado, atualiza o campo de texto com o caminho.
        if fileName:  
            self.uiFilePath.setText(fileName)  

    # Método para converter o arquivo .ui para .py:
    def convert_file(self):
        # Obtém o caminho do arquivo .ui do campo de texto.
        ui_file = self.uiFilePath.text()  
        # Verifica se o arquivo tem a extensão correta (.ui).
        if not ui_file.endswith('.ui'):   
            # Exibe mensagem de erro caso a extensão seja inválida.
            QMessageBox.warning(self, "Erro", "Por favor Selecione o arquivo .ui valido")  
            return  # Sai da função se o arquivo for inválido.

        # Define o caminho do arquivo .py (substituindo a extensão).
        py_file = ui_file.replace('.ui', '.py')  

        # Verificando se o comando pyuic5 está disponível
        if not shutil.which("pyuic5"):
            QMessageBox.critical(self, "Erro", "Comando pyuic5 não encontrado. Certifique-se de que o PyQt5 esteja instalado.")
            return

        # Tentativa de converter o arquivo "Se"
        try:
            result = os.system(f'pyuic5 "{ui_file}" -o "{py_file}"')
            if result == 0:
                QMessageBox.information(self, "Successo", f"O Arquivo foi convertido e salvo na {py_file}")
            else:
                QMessageBox.critical(self, "Error", f"Ocorreu um erro durante a conversão. Verifique o caminho do arquivo e a instalação do pyuic5.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Um erro ocorreu {str(e)}")

# Bloco de código executado quando o script é rodado diretamente:
if __name__ == '__main__':
    # Importa o módulo shutil para manipulação de arquivos.
    import shutil 

    # Cria a aplicação PyQt5.
    app = QApplication(sys.argv)  
    # Cria uma instância da janela principal.
    window = ConverterUI()  
    # Exibe a janela.
    window.show()  
    # Inicia o loop de eventos da aplicação e encerra quando a janela é fechada.
    sys.exit(app.exec_())  
