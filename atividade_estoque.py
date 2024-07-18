class Voluntario:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class BancoAlimentos:
    def __init__(self):
        self.voluntarios = []
        self.doacoes = {}

    def registrar_voluntario(self, nome, telefone):
        voluntario = Voluntario(nome, telefone)
        self.voluntarios.append(voluntario)
        print(f"Voluntário {nome} registrado com sucesso.")

    def registrar_doacao(self, item, quantidade):
        if item in self.doacoes:
            self.doacoes[item] += quantidade
        else:
            self.doacoes[item] = quantidade
        print(f"{quantidade} unidades de {item} registradas no banco de alimentos.")

    def listar_voluntarios(self):
        print("Lista de Voluntários:")
        for voluntario in self.voluntarios:
            print(f"Nome: {voluntario.nome}, Telefone: {voluntario.telefone}")

    def mostrar_estoque(self):
        print("Estoque de Alimentos:")
        for item, quantidade in self.doacoes.items():
            print(f"{item}: {quantidade} unidades")

# Função para interação com o usuário
def interface_usuario():
    banco_alimentos = BancoAlimentos()

    while True:
        print("\n### Menu ###")
        print("1. Registrar Voluntário")
        print("2. Registrar Doação")
        print("3. Listar Voluntários")
        print("4. Mostrar Estoque")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do voluntário: ")
            telefone = input("Digite o telefone do voluntário: ")
            banco_alimentos.registrar_voluntario(nome, telefone)

        elif opcao == "2":
            item = input("Digite o nome do item doado: ")
            quantidade = int(input("Digite a quantidade doada: "))
            banco_alimentos.registrar_doacao(item, quantidade)

        elif opcao == "3":
            banco_alimentos.listar_voluntarios()

        elif opcao == "4":
            banco_alimentos.mostrar_estoque()

        elif opcao == "5":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    interface_usuario()
