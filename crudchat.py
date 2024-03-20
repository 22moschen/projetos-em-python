import csv

# Define o nome do arquivo CSV utilizado para armazenar os dados dos clientes
ARQUIVO_CLIENTES = "clientes.csv"

# Função para criar o arquivo CSV se ele ainda não existir
def criar_arquivo():
    try:
        with open(ARQUIVO_CLIENTES, "x") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["id", "nome", "email", "telefone"])
            print("Arquivo criado com sucesso!")
    except FileExistsError:
        pass

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    with open(ARQUIVO_CLIENTES, "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        writer.writerow([obter_proximo_id(), nome, email, telefone])
        print("Cliente cadastrado com sucesso!")

# Função para obter o próximo ID disponível para um novo cliente
def obter_proximo_id():
    try:
        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            reader = csv.reader(arquivo)
            ids = [int(row[0]) for row in reader][1:]
            return max(ids) + 1
    except FileNotFoundError:
        return 1

# Função para listar todos os clientes cadastrados
def listar_clientes():
    try:
        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            reader = csv.reader(arquivo)
            for row in reader:
                print(f"ID: {row[0]} | Nome: {row[1]} | E-mail: {row[2]} | Telefone: {row[3]}")
    except FileNotFoundError:
        print("Não há clientes cadastrados.")

# Função para atualizar os dados de um cliente existente
def atualizar_cliente():
    id_cliente = input("Digite o ID do cliente que deseja atualizar: ")
    try:
        with open(ARQUIVO_CLIENTES, "r") as arquivo:
            reader = csv.reader(arquivo)
            dados = [row for row in reader]
            for i, row in enumerate(dados):
                if row[0] == id_cliente:
                    nome = input(f"Digite o novo nome do cliente ({row[1]}): ")
                    email = input(f"Digite o novo e-mail do cliente ({row[2]}): ")
                    telefone = input(f"Digite o novo telefone do cliente ({row[3]}): ")
                    dados[i] = [id_cliente, nome or row[1], email or row[2], telefone or row[3]]
                    break
            else:
                print(f"Não foi encontrado um cliente com o ID {id_cliente}.")
                return
        with open(ARQUIVO_CLIENTES, "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(dados)
            print("Dados do cliente atualizados com sucesso!")
    except FileNotFoundError:
        print("Não há clientes cadastrados.")

# Função para excluir um cliente existente
# def excluir_cliente():
   # id_cliente = input("Digite o ID do cliente que deseja excluir: ")
   # try:
  #      with open(ARQUIVO_CLIENTES, "r") as arquivo:
 #          reader = csv.reader(arquivo)
