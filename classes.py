import os
import random

class Receita:
    def __init__(self, nome, origem, ingredientes, modo_de_preparo):
        self.nome = nome
        self.origem = origem
        self.ingredientes = ingredientes
        self.modo_de_preparo = modo_de_preparo
    
    #Adicionar nova receita
    def adicionar(self, receita):
        file = open(f"Receitas/{(receita.nome).strip()}.txt", "a")

        file.write(f"""Nome: {receita.nome}\n\nOrigem: {receita.origem}\n\nIngredientes:\n""")

        for ingrediente in receita.ingredientes:
            file.write(f"   - {(ingrediente).capitalize()}\n")
        #file.writelines("\n".join(receita.ingredientes).capitalize())
        
        file.write(f"\nModo de preparo: {receita.modo_de_preparo}")

        file.close()

        print("\nReceita criada com sucesso!")
        #cria o arquivo .txt em branco
        #write as infos da Receita
        #close arquivo
    
    def visualizarTodas():
        #abre o diretório (pasta) Receitas
        pasta_receitas = os.listdir("Receitas")

        print("=========== Lista de Receitas ===========")
        #printa as receitas (todos os arquivos da pasta, removendo a extensão .txt no nome) do diretório Receitas
        for receita in pasta_receitas:
             print(os.path.splitext(receita)[0])

    def buscarReceita(receita):
        pasta_receitas = os.listdir("Receitas")

        nome_arquivo = f"{receita}.txt"
        #verifica se a receita do input do usuário está no diretório Receitas
        if nome_arquivo in pasta_receitas:
            file = open(f"./Receitas/{nome_arquivo}", "r")
            print(file.read())
            file.close()
        
        else:
            print("\nReceita não encontrada.")
    
    def sugerirReceita():
        lista_receitas = []
        pasta_receitas = os.listdir("Receitas")

        for receita in pasta_receitas:
            lista_receitas.append(os.path.splitext(receita)[0])
        
        sugestao = random.choice(lista_receitas)
        print(f"Receita sugerida: {sugestao}")

        return sugestao
