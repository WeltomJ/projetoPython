import os  # Importa o módulo 'os' para operações relacionadas ao sistema operacional
import datetime  # Importa o módulo 'datetime' para trabalhar com datas e horas
import tkinter as tk  # Importa a biblioteca tkinter para criar a interface gráfica
from tkinter import scrolledtext, messagebox  # Importa componentes específicos do tkinter
import tkinter.ttk as ttk  # Importa o módulo ttk para widgets com estilo melhorado


class DiarioApp:  # Define a classe principal da aplicação gráfica
    def __init__(self, root):  # Método construtor que inicializa a aplicação
        self.root = root  # Armazena a referência da janela principal
        self.root.title("Diário Pessoal")  # Define o título da janela
        self.root.geometry("800x600")  # Define o tamanho inicial da janela
        self.root.minsize(600, 400)  # Define o tamanho mínimo da janela

        # Configura o estilo e aparência
        self.configurar_estilo()  # Chama o método que configura os estilos

        # Cria o layout principal
        self.criar_layout()  # Chama o método que cria o layout da interface

    def configurar_estilo(self):  # Método para configurar os estilos da aplicação
        # Define cores e estilos para a interface
        self.cor_fundo = "#f5f5f5"  # Cor de fundo clara
        self.cor_destaque = "#4a6fa5"  # Cor de destaque azul
        self.cor_texto = "#333333"  # Cor do texto principal

        # Configura a cor de fundo da janela principal
        self.root.configure(bg=self.cor_fundo)

        # Configura os estilos dos widgets ttk
        style = ttk.Style()  # Cria um objeto de estilo
        style.theme_use("clam")  # Usa um tema mais moderno
        style.configure("TButton", font=("Arial", 11), background=self.cor_destaque)  # Estilo para botões
        style.configure("TLabel", font=("Arial", 12), background=self.cor_fundo)  # Estilo para labels
        style.configure("Header.TLabel", font=("Arial", 16, "bold"),
                        background=self.cor_fundo)  # Estilo para cabeçalhos

        # Estilo personalizado para botões
        style.configure("Accent.TButton", font=("Arial", 11, "bold"), background="#2a416a")

    def criar_layout(self):  # Método para criar o layout da interface
        # Frame principal que contém todos os componentes
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)  # Cria o frame principal
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Posiciona o frame na janela

        # Título da aplicação
        header_label = ttk.Label(
            main_frame,
            text="✨ DIÁRIO PESSOAL ✨",
            style="Header.TLabel"
        )  # Cria o label do cabeçalho
        header_label.pack(pady=(0, 20))  # Posiciona o cabeçalho

        # Frame para os botões
        buttons_frame = tk.Frame(main_frame, bg=self.cor_fundo)  # Cria um frame para os botões
        buttons_frame.pack(fill=tk.X, pady=10)  # Posiciona o frame de botões

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
        self.status_var = tk.StringVar()  # Variável para conter o texto do status
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

    def mostrar_boas_vindas(self):  # Método para exibir a tela de boas-vindas
        # Limpa o frame de conteúdo
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Remove todos os widgets filhos

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

    def nova_entrada(self):  # Método para criar uma nova entrada no diário
        # Limpa o frame de conteúdo
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Remove todos os widgets filhos

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

    def salvar_entrada(self):  # Método para salvar a entrada do diário
        # Obtém o texto digitado
        texto = self.text_entrada.get("1.0", tk.END).strip()  # Obtém todo o texto da área de texto

        if not texto:  # Verifica se o texto está vazio
            messagebox.showwarning("Aviso", "Por favor, digite algo antes de salvar.")  # Mostra aviso
            return  # Interrompe o método

        # Obtém a data e hora atual formatada
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Formata data e hora

        try:
            # Abre o arquivo do diário em modo de anexação (append)
            with open("diario.txt", "a", encoding="utf-8") as arquivo:
                # Escreve a entrada no arquivo com data e hora
                arquivo.write(f"[{data_hora}] {texto}\n\n")  # Escreve a entrada no arquivo

            # Mostra mensagem de sucesso
            messagebox.showinfo("Sucesso", "✅ Entrada salva com sucesso!")  # Mostra mensagem de sucesso

            # Volta para tela inicial
            self.mostrar_boas_vindas()  # Retorna para a tela inicial
            self.status_var.set("Entrada salva com sucesso")  # Atualiza o texto de status

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar entrada: {str(e)}")  # Mostra erro
            self.status_var.set("Erro ao salvar")  # Atualiza o texto de status

    def ler_diario(self):  # Método para ler o conteúdo do diário
        # Limpa o frame de conteúdo
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Remove todos os widgets filhos

        # Cria e exibe o frame para leitura do diário
        read_frame = tk.Frame(self.content_frame, bg=self.cor_fundo)  # Cria frame para leitura
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
        )  # Cria área de texto para mostrar o diário
        text_diario.pack(fill=tk.BOTH, expand=True, pady=10)  # Posiciona a área de texto

        # Verifica se o arquivo do diário existe
        if not os.path.exists("diario.txt"):  # Verifica se o arquivo existe
            text_diario.insert(tk.END, "O diário ainda está vazio. Faça sua primeira anotação!")  # Insere mensagem
            self.status_var.set("Diário vazio")  # Atualiza o texto de status
        else:
            try:
                # Abre o arquivo do diário em modo de leitura
                with open("diario.txt", "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()  # Lê todo o conteúdo

                    if conteudo.strip() == "":  # Verifica se o conteúdo está vazio
                        text_diario.insert(tk.END, "O diário está vazio. Adicione algumas entradas!")  # Insere mensagem
                    else:
                        text_diario.insert(tk.END, conteudo)  # Insere o conteúdo do diário

                self.status_var.set("Diário carregado com sucesso")  # Atualiza o texto de status
            except Exception as e:
                text_diario.insert(tk.END, f"Erro ao ler o diário: {str(e)}")  # Insere mensagem de erro
                self.status_var.set("Erro ao ler o diário")  # Atualiza o texto de status

        # Configura a área de texto como somente leitura
        text_diario.configure(state="disabled")  # Desabilita edição

        # Botão para voltar
        btn_voltar = ttk.Button(
            read_frame,
            text="Voltar",
            command=self.mostrar_boas_vindas
        )  # Cria botão para voltar
        btn_voltar.pack(pady=10)  # Posiciona o botão


def main():  # Define a função principal do programa
    root = tk.Tk()  # Cria a janela principal
    root.tk.call('tk', 'scaling', 1.2)  # Aumenta ligeiramente o tamanho de todos os elementos
    app = DiarioApp(root)  # Instancia a aplicação
    root.mainloop()  # Inicia o loop de eventos da interface


if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal para iniciar o programa
