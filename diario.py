import os  # Importa o módulo os para manipulação de arquivos e diretórios
import datetime  # Importa o módulo datetime para trabalhar com datas e horas
import tkinter as tk  # Importa o tkinter para criar interfaces gráficas
from tkinter import scrolledtext, messagebox  # Importa widgets específicos do tkinter
import tkinter.ttk as ttk  # Importa o ttk para widgets com estilos aprimorados
import sqlite3  # Importa o módulo sqlite3 para manipulação de banco de dados SQLite

class DiarioApp:  # Define a classe principal do aplicativo
    def __init__(self, root):  # Método construtor da classe
        self.root = root  # Guarda a referência da janela principal
        self.root.title("Diário Pessoal")  # Define o título da janela
        self.root.geometry("800x600")  # Define o tamanho inicial da janela
        self.root.minsize(600, 400)  # Define o tamanho mínimo da janela
        
        # Configura o estilo e aparência
        self.configurar_estilo()  # Chama o método para configurar estilos
        
        # Inicializa o banco de dados SQLite
        self.inicializar_banco()  # Chama o método para inicializar o banco
        
        # Cria o layout principal
        self.criar_layout()  # Chama o método para criar o layout
    
    def inicializar_banco(self):  # Método para inicializar o banco de dados
        """Inicializa a conexão com o banco de dados SQLite."""
        # Define o caminho do banco de dados
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diario.db")  # Caminho do arquivo do banco
        
        # Cria a conexão e a tabela se não existir
        try:  # Tenta executar o bloco
            self.conn = sqlite3.connect(self.db_path)  # Cria a conexão com o banco
            self.cursor = self.conn.cursor()  # Cria o cursor para executar comandos SQL
            
            # Cria a tabela entradas se não existir
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS entradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_hora TEXT NOT NULL,
                    conteudo TEXT NOT NULL
                )
            ''')
            self.conn.commit()  # Salva as alterações no banco
            
        except sqlite3.Error as e:  # Captura erros do SQLite
            messagebox.showerror("Erro de Banco de Dados", f"Não foi possível inicializar o banco de dados: {str(e)}")  # Mostra mensagem de erro
    
    def configurar_estilo(self):  # Método para configurar estilos visuais
        # Define cores e estilos para a interface
        self.cor_fundo = "#f5f5f5"  # Cor de fundo clara
        self.cor_destaque = "#4a6fa5"  # Cor de destaque azul
        self.cor_texto = "#333333"  # Cor do texto principal
        
        # Configura a cor de fundo da janela principal
        self.root.configure(bg=self.cor_fundo)  # Aplica a cor de fundo
        
        # Configura os estilos dos widgets ttk
        style = ttk.Style()  # Cria um objeto de estilo
        style.theme_use("clam")  # Usa o tema 'clam'
        style.configure("TButton", font=("Arial", 11), background=self.cor_destaque)  # Estilo para botões
        style.configure("TLabel", font=("Arial", 12), background=self.cor_fundo)  # Estilo para labels
        style.configure("Header.TLabel", font=("Arial", 16, "bold"), background=self.cor_fundo)  # Estilo para cabeçalhos
        
        # Estilo personalizado para botões
        style.configure("Accent.TButton", font=("Arial", 11, "bold"), background="#2a416a")  # Botão de destaque
    
    def criar_layout(self):  # Método para criar o layout da interface
        # Frame principal que contém todos os componentes
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)  # Cria o frame principal
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Posiciona o frame
        
        # Título da aplicação
        header_label = ttk.Label(
            main_frame, 
            text="✨ DIÁRIO PESSOAL ✨", 
            style="Header.TLabel"
        )  # Cria o label do cabeçalho
        header_label.pack(pady=(0, 20))  # Posiciona o cabeçalho
        
        # Frame para os botões
        buttons_frame = tk.Frame(main_frame, bg=self.cor_fundo)  # Cria um frame para os botões
        buttons_frame.pack(fill=tk.X, pady=10)  # Posiciona o frame
        
        # Botões de ação
        self.btn_nova_entrada = ttk.Button(
            buttons_frame, 
            text="✏️ Nova Entrada", 
            command=self.nova_entrada,
            style="Accent.TButton"
        )  # Cria o botão de nova entrada
        self.btn_nova_entrada.pack(side=tk.LEFT, padx=5)  # Posiciona o botão
        
        self.btn_ler_diario = ttk.Button(
            buttons_frame, 
            text="📖 Ler Diário", 
            command=self.ler_diario
        )  # Cria o botão de ler diário
        self.btn_ler_diario.pack(side=tk.LEFT, padx=5)  # Posiciona o botão
        
        # Frame para conteúdo dinâmico
        self.content_frame = tk.Frame(main_frame, bg=self.cor_fundo)  # Cria o frame de conteúdo
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=10)  # Posiciona o frame
        
        # Barra de status na parte inferior
        self.status_var = tk.StringVar()  # Variável para o texto do status
        self.status_var.set("Pronto")  # Define o status inicial
        status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )  # Cria a barra de status
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)  # Posiciona a barra de status
        
        # Inicialmente, mostra a tela de boas-vindas
        self.mostrar_boas_vindas()  # Chama o método para mostrar a tela inicial
    
    def mostrar_boas_vindas(self):  # Método para mostrar a tela de boas-vindas
        # Limpa o frame de conteúdo
        for widget in self.content_frame.winfo_children():  # Percorre todos os widgets filhos
            widget.destroy()  # Remove o widget
        
        # Cria e exibe a mensagem de boas-vindas
        welcome_frame = tk.Frame(self.content_frame, bg=self.cor_fundo)  # Cria um frame para as boas-vindas
        welcome_frame.pack(fill=tk.BOTH, expand=True)  # Posiciona o frame
        
        # Label de boas-vindas
        welcome_label = ttk.Label(
            welcome_frame, 
            text="Bem-vindo ao seu Diário Pessoal!",
            font=("Arial", 16, "bold"),
            background=self.cor_fundo
        )  # Cria o label de boas-vindas
        welcome_label.pack(pady=50)  # Posiciona o label
        
        # Instruções para o usuário
        instruction_label = ttk.Label(
            welcome_frame,
            text="Escreva seus pensamentos e reflexões ou reveja momentos importantes.\n"
                 "Selecione 'Nova Entrada' para escrever ou 'Ler Diário' para visualizar suas anotações.",
            wraplength=500,
            background=self.cor_fundo
        )  # Cria o label de instruções
        instruction_label.pack()  # Posiciona o label
        
        # Atualiza a barra de status
        self.status_var.set("Pronto para registrar seus pensamentos")  # Atualiza o texto de status
    
    def nova_entrada(self):  # Método para criar uma nova entrada
        # Limpa o frame de conteúdo
        for widget in self.content_frame.winfo_children():  # Percorre todos os widgets filhos
            widget.destroy()  # Remove o widget
        
        # Cria e exibe o formulário para nova entrada
        entry_frame = tk.Frame(self.content_frame, bg=self.cor_fundo)  # Cria um frame para a nova entrada
        entry_frame.pack(fill=tk.BOTH, expand=True)  # Posiciona o frame
        
        # Título
        title_label = ttk.Label(
            entry_frame, 
            text="✏️ Nova Entrada no Diário", 
            style="Header.TLabel"
        )  # Cria o label de título
        title_label.pack(pady=10)  # Posiciona o label
        
        # Data atual
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")  # Formata a data atual
        date_label = ttk.Label(
            entry_frame,
            text=f"Data: {data_atual}",
            background=self.cor_fundo
        )  # Cria o label de data
        date_label.pack(anchor=tk.W, pady=(0, 10))  # Posiciona o label
        
        # Área de texto com barra de rolagem
        self.text_entrada = scrolledtext.ScrolledText(
            entry_frame, 
            wrap=tk.WORD, 
            font=("Arial", 11),
            height=15
        )  # Cria a área de texto
        self.text_entrada.pack(fill=tk.BOTH, expand=True, pady=10)  # Posiciona a área de texto
        self.text_entrada.focus_set()  # Coloca o cursor na área de texto
        
        # Frame para botões inferiores
        buttons_frame = tk.Frame(entry_frame, bg=self.cor_fundo)  # Cria frame para botões
        buttons_frame.pack(fill=tk.X, pady=10)  # Posiciona o frame
        
        # Botão para cancelar
        btn_cancelar = ttk.Button(
            buttons_frame, 
            text="Cancelar", 
            command=self.mostrar_boas_vindas
        )  # Cria o botão de cancelar
        btn_cancelar.pack(side=tk.LEFT, padx=5)  # Posiciona o botão
        
        # Botão para salvar
        btn_salvar = ttk.Button(
            buttons_frame, 
            text="Salvar Entrada", 
            command=self.salvar_entrada,
            style="Accent.TButton"
        )  # Cria o botão de salvar
        btn_salvar.pack(side=tk.RIGHT, padx=5)  # Posiciona o botão
        
        # Atualiza a barra de status
        self.status_var.set("Digite sua nova entrada...")  # Atualiza o texto de status
    
    def salvar_entrada(self):  # Método para salvar uma entrada no banco
        # Obtém o texto digitado
        texto = self.text_entrada.get("1.0", tk.END).strip()  # Pega o texto da área de entrada
        
        if not texto:  # Verifica se o texto está vazio
            messagebox.showwarning("Aviso", "Por favor, digite algo antes de salvar.")  # Mostra aviso
            return  # Sai da função
        
        # Obtém a data e hora atual formatada
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formata data e hora
        
        try:  # Tenta executar o bloco
            # Salva a entrada no banco de dados SQLite
            self.cursor.execute(
                "INSERT INTO entradas (data_hora, conteudo) VALUES (?, ?)",
                (data_hora, texto)
            )  # Executa o comando SQL
            self.conn.commit()  # Salva as alterações
            
            # Mostra mensagem de sucesso
            messagebox.showinfo("Sucesso", "✅ Entrada salva com sucesso no banco de dados!")  # Mostra mensagem
            
            # Volta para tela inicial
            self.mostrar_boas_vindas()  # Chama tela inicial
            self.status_var.set("Entrada salva com sucesso no banco de dados")  # Atualiza status
            
        except sqlite3.Error as e:  # Captura erro do SQLite
            messagebox.showerror("Erro", f"Erro ao salvar entrada: {str(e)}")  # Mostra erro
            self.status_var.set("Erro ao salvar no banco de dados")  # Atualiza status
    
    def ler_diario(self):  # Método para ler as entradas do diário
        # Limpa o frame de conteúdo
        for widget in self.content_frame.winfo_children():  # Percorre todos os widgets filhos
            widget.destroy()  # Remove o widget
        
        # Cria e exibe o frame para leitura do diário
        read_frame = tk.Frame(self.content_frame, bg=self.cor_fundo)  # Cria frame de leitura
        read_frame.pack(fill=tk.BOTH, expand=True)  # Posiciona o frame
        
        # Título
        title_label = ttk.Label(
            read_frame, 
            text="📖 Minhas Entradas", 
            style="Header.TLabel"
        )  # Cria o label de título
        title_label.pack(pady=10)  # Posiciona o label
        
        # Área de texto com barra de rolagem (somente leitura)
        text_diario = scrolledtext.ScrolledText(
            read_frame, 
            wrap=tk.WORD, 
            font=("Arial", 11),
            height=20
        )  # Cria a área de texto
        text_diario.pack(fill=tk.BOTH, expand=True, pady=10)  # Posiciona a área de texto
        
        try:  # Tenta executar o bloco
            # Consulta as entradas no banco de dados, ordenadas da mais recente para mais antiga
            self.cursor.execute("SELECT data_hora, conteudo FROM entradas ORDER BY data_hora DESC")  # Executa consulta SQL
            entradas = self.cursor.fetchall()  # Busca todos os resultados
            
            if not entradas:  # Se não houver entradas
                text_diario.insert(tk.END, "O diário ainda está vazio. Faça sua primeira anotação!")  # Mensagem de diário vazio
                self.status_var.set("Diário vazio")  # Atualiza status
            else:  # Se houver entradas
                # Formata e exibe cada entrada
                for data_hora, conteudo in entradas:  # Para cada entrada
                    text_diario.insert(tk.END, f"[{data_hora}]\n")  # Insere data/hora
                    text_diario.insert(tk.END, f"{conteudo}\n\n")  # Insere conteúdo
                    text_diario.insert(tk.END, "-" * 50 + "\n\n")  # Insere separador
                
                self.status_var.set(f"Diário carregado com sucesso. Total: {len(entradas)} entradas.")  # Atualiza status
                
        except sqlite3.Error as e:  # Captura erro do SQLite
            text_diario.insert(tk.END, f"Erro ao ler o diário: {str(e)}")  # Mostra erro
            self.status_var.set("Erro ao ler o banco de dados")  # Atualiza status
        
        # Configura a área de texto como somente leitura
        text_diario.configure(state="disabled")  # Torna a área de texto somente leitura
        
        # Botão para voltar
        btn_voltar = ttk.Button(
            read_frame, 
            text="Voltar", 
            command=self.mostrar_boas_vindas
        )  # Cria o botão de voltar
        btn_voltar.pack(pady=10)  # Posiciona o botão
    
    def __del__(self):  # Destrutor para fechar a conexão com o banco
        """Destrutor para garantir fechamento da conexão com o banco."""
        try:  # Tenta executar o bloco
            if hasattr(self, 'conn') and self.conn:  # Verifica se a conexão existe
                self.conn.close()  # Fecha a conexão
        except:  # Captura qualquer erro
            pass  # Ignora erros

def main():  # Função principal do programa
    root = tk.Tk()  # Cria a janela principal do tkinter
    root.tk.call('tk', 'scaling', 1.2)  # Ajusta a escala da interface
    app = DiarioApp(root)  # Cria a aplicação
    root.mainloop()  # Inicia o loop principal da interface


if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal
