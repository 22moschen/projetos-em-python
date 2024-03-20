import csv

ARQUIVO_CLIENTES = "clientes.csv"

def criar_arquivo():
    try:
        with open(ARQUIVO_CLIENTES, "x") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["id", "nome", "email", "telefone"])
            print("Arquivo criado com sucesso! :)")
    except FileExistsError:
        pass

def cadastrar_cliente():
    with open(ARQUIVO_CLIENTES, "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        writer.writerow([obter_proximo_id(), nome, email, telefone])
        print("Cliente cadastrado com sucesso!")


def obter_proximo_id():
    try:
        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            reader = csv.reader(arquivo)

            # Ignora a primeira linha (cabeçalho)
            next(reader, None)

            # Obtém os IDs a partir da segunda linha
            ids = [int(row[0]) for row in reader if row]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1


def listar_clientes():
    try:
        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            reader = csv.reader(arquivo)
            # Ignora a primeira linha (cabeçalho)
            next(reader, None)

            for row in reader:
                if len(row) >= 4:
                    print(f"ID: {row[0]} | Nome: {row[1]} | E-mail: {row[2]} | Telefone: {row[3]}")
                else:
                    print("Formato inválido no arquivo CSV.")
    except FileNotFoundError:
        print("Não há clientes cadastrados!")


def main():
    criar_arquivo()

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
