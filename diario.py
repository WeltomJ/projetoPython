import os  # Importa o módulo 'os' para operações relacionadas ao sistema operacional
import datetime  # Importa o módulo 'datetime' para trabalhar com datas e horas


def mostrar_menu():  # Define a função que exibe o menu principal
    print("\n===== DIÁRIO PESSOAL =====")  # Imprime o título do aplicativo
    print("1. Escrever no diário")  # Imprime a opção 1 do menu
    print("2. Ler o diário")  # Imprime a opção 2 do menu
    print("3. Sair")  # Imprime a opção 3 do menu
    return input("Escolha uma opção (1-3): ")  # Solicita e retorna a escolha do usuário


def escrever_no_diario():  # Define a função para escrever uma nova entrada no diário
    print("\n--- Nova Entrada no Diário ---")  # Imprime o cabeçalho da seção
    texto = input("Digite seu pensamento ou anotação:\n")  # Solicita ao usuário o texto da entrada

    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Obtém a data e hora atual formatada

    with open("diario.txt", "a", encoding="utf-8") as arquivo:  # Abre o arquivo do diário em modo de anexação (append)
        arquivo.write(f"[{data_hora}] {texto}\n\n")  # Escreve a entrada no arquivo com data e hora

    print("✓ Entrada salva com sucesso!")  # Confirma ao usuário que a entrada foi salva


def ler_diario():  # Define a função para ler o conteúdo do diário
    print("\n--- Lendo Diário ---")  # Imprime o cabeçalho da seção

    if not os.path.exists("diario.txt"):  # Verifica se o arquivo do diário existe
        print("O diário ainda está vazio. Faça sua primeira anotação!")  # Informa que o diário está vazio
        return  # Sai da função

    with open("diario.txt", "r", encoding="utf-8") as arquivo:  # Abre o arquivo do diário em modo de leitura
        conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

        if conteudo.strip() == "":  # Verifica se o conteúdo está vazio (após remover espaços)
            print("O diário está vazio. Adicione algumas entradas!")  # Informa que o diário está vazio
        else:
            print(conteudo)  # Imprime todo o conteúdo do diário


def main():  # Define a função principal do programa
    print("Bem-vindo ao seu Diário Pessoal!")  # Imprime mensagem de boas-vindas

    while True:  # Inicia um loop infinito que só termina quando o usuário escolher sair
        opcao = mostrar_menu()  # Chama a função do menu e armazena a escolha do usuário

        if opcao == "1":  # Verifica se o usuário escolheu a opção 1
            escrever_no_diario()  # Chama a função para escrever no diário
        elif opcao == "2":  # Verifica se o usuário escolheu a opção 2
            ler_diario()  # Chama a função para ler o diário
        elif opcao == "3":  # Verifica se o usuário escolheu a opção 3
            print("\nObrigado por usar o Diário Pessoal. Até a próxima!")  # Imprime mensagem de despedida
            break  # Sai do loop infinito, encerrando o programa
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")  # Informa que a opção é inválida


if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal para iniciar o programa
