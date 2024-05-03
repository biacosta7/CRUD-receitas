class Receita:
    def __init__(self, nome, origem, ingredientes, modo_de_preparo):
        self.nome = nome
        self.origem = origem
        self.ingredientes = ingredientes
        self.modo_de_preparo = modo_de_preparo
    
    def adicionar(self, receita):
        file = open(f"Receitas/{(receita.nome).strip()}.txt", "a")

        file.write(f"""Nome: {receita.nome}\n
Origem: {receita.origem}\n
Ingredientes:\n""")
        for ingrediente in self.ingredientes:
                file.write(f"   - {(ingrediente).capitalize()}\n")
        file.write(f"\nModo de preparo: {receita.modo_de_preparo}")

        file.close()

        print("\nReceita criada com sucesso!")
        #cria o arquivo .txt em branco
        #write as infos da Receita
        #close arquivo

