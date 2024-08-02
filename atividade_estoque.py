import tkinter as tk
from tkinter import messagebox

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
        messagebox.showinfo("Registro de Voluntário", f"Voluntário {nome} registrado com sucesso.")

    def registrar_doacao(self, item, quantidade):
        if item in self.doacoes:
            self.doacoes[item] += quantidade
        else:
            self.doacoes[item] = quantidade
        messagebox.showinfo("Registro de Doação", f"{quantidade} unidades de {item} registradas no banco de alimentos.")

    def listar_voluntarios(self):
        lista = "\n".join([f"Nome: {v.nome}, Telefone: {v.telefone}" for v in self.voluntarios])
        messagebox.showinfo("Lista de Voluntários", lista or "Nenhum voluntário registrado.")

    def mostrar_estoque(self):
        estoque = "\n".join([f"{item}: {quantidade} unidades" for item, quantidade in self.doacoes.items()])
        messagebox.showinfo("Estoque de Alimentos", estoque or "Estoque vazio.")

class InterfaceBancoAlimentos:
    def __init__(self, root):
        self.banco_alimentos = BancoAlimentos()
        
        self.root = root
        self.root.title("Banco de Alimentos")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=10)

        self.label = tk.Label(self.main_frame, text="Escolha uma opção:")
        self.label.pack(pady=5)

        self.btn_registrar_voluntario = tk.Button(self.main_frame, text="Registrar Voluntário", command=self.registrar_voluntario)
        self.btn_registrar_voluntario.pack(pady=5)

        self.btn_registrar_doacao = tk.Button(self.main_frame, text="Registrar Doação", command=self.registrar_doacao)
        self.btn_registrar_doacao.pack(pady=5)

        self.btn_listar_voluntarios = tk.Button(self.main_frame, text="Listar Voluntários", command=self.listar_voluntarios)
        self.btn_listar_voluntarios.pack(pady=5)

        self.btn_mostrar_estoque = tk.Button(self.main_frame, text="Mostrar Estoque", command=self.mostrar_estoque)
        self.btn_mostrar_estoque.pack(pady=5)

        self.btn_sair = tk.Button(self.main_frame, text="Sair", command=root.quit)
        self.btn_sair.pack(pady=5)

    def registrar_voluntario(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Voluntário")

        tk.Label(top, text="Nome:").pack(pady=5)
        nome = tk.Entry(top)
        nome.pack(pady=5)

        tk.Label(top, text="Telefone:").pack(pady=5)
        telefone = tk.Entry(top)
        telefone.pack(pady=5)

        def confirmar():
            self.banco_alimentos.registrar_voluntario(nome.get(), telefone.get())
            top.destroy()

        tk.Button(top, text="Registrar", command=confirmar).pack(pady=10)

    def registrar_doacao(self):
        top = tk.Toplevel(self.root)
        top.title("Registrar Doação")

        tk.Label(top, text="Item:").pack(pady=5)
        item = tk.Entry(top)
        item.pack(pady=5)

        tk.Label(top, text="Quantidade:").pack(pady=5)
        quantidade = tk.Entry(top)
        quantidade.pack(pady=5)

        def confirmar():
            self.banco_alimentos.registrar_doacao(item.get(), int(quantidade.get()))
            top.destroy()

        tk.Button(top, text="Registrar", command=confirmar).pack(pady=10)

    def listar_voluntarios(self):
        self.banco_alimentos.listar_voluntarios()

    def mostrar_estoque(self):
        self.banco_alimentos.mostrar_estoque()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceBancoAlimentos(root)
    root.mainloop()
    