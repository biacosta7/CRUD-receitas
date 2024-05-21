import os
import random

class Receita:
    global pasta_receitas
    pasta_receitas = os.listdir("./Receitas")

    def __init__(self, nome, origem, ingredientes, modo_de_preparo):
        self.nome = nome
        self.origem = origem
        self.ingredientes = ingredientes
        self.modo_de_preparo = modo_de_preparo
    
    #Adicionar nova receita
    def adicionar(self, receita):
        file = open(f"./Receitas/{(receita.nome).strip()}.txt", "a")

        file.write(f"""Nome: {receita.nome}\n\nOrigem: {receita.origem}\n\nIngredientes:\n""")

        for ingrediente in receita.ingredientes:
            file.write(f"   - {(ingrediente).capitalize()}\n")
        
        file.write(f"\nModo de preparo: {receita.modo_de_preparo}")

        file.close()

        print("\nReceita criada com sucesso!")
        #cria o arquivo .txt em branco
        #write as infos da Receita
        #close arquivo
    
    def visualizarTodas():
        global pasta_receitas
        pasta_receitas = os.listdir("./Receitas")

        print("=========== Lista de Receitas ===========")
        #printa as receitas (todos os arquivos da pasta, removendo a extensão .txt no nome) do diretório Receitas
        for receita in pasta_receitas:
            print(os.path.splitext(receita)[0])

    def buscarReceita(receita):

        nome_arquivo = f"{receita}.txt"
        #verifica se a receita do input do usuário está no diretório Receitas
        if nome_arquivo in pasta_receitas:
            file = open(f"./Receitas/{nome_arquivo}", "r")
            print(file.read())
            file.close()
        
        else:
            print("\nReceita não encontrada.")
    
    def exclusao(receita):
        try:
            nome_arquivo = f"{receita}.txt"
            os.remove(f"./Receitas/{nome_arquivo}")
        except FileNotFoundError:
            print("Receita não encontrada.")

    def filtrarPais(pais):
        paisreceita = {}

        for receita in pasta_receitas:
            nome_arquivo = f"{receita}"
            file = open(f"./Receitas/{nome_arquivo}", "r")
            lines = file.readlines()
            file.close()
            for line in lines:
                if line.strip() == f"Origem: {pais.capitalize()}":
                    if pais in paisreceita:
                        paisreceita[pais].append(receita)
                    else:
                        paisreceita[pais] = [receita]
        if pais in paisreceita:
            if pais.endswith("a"):
                print(f"\n=========== Lista de Receitas da {pais} ===========")
                for receita in paisreceita[pais]:
                    print(os.path.splitext(receita)[0])
            else:
                print(f"\n=========== Lista de Receitas do {pais} ===========")
                for receita in paisreceita[pais]:
                    print(os.path.splitext(receita)[0])
        else:
            print("O país selecionado ainda não possui receitas a apresentar.")
        
        return paisreceita

    def mostrarmenu():
        print("Menu:")
        print("1. Adicionar receita aos favoritos")
        print("2. Ver receitas favoritas")
        print("3. Sair")

    def adicionarfavorito(favoritos):
        pasta_receitas = os.listdir("Receitas")
        receita = input("Digite o nome da receita que deseja adicionar aos favoritos (sem extensão): ").capitalize()

        nome_arquivo = f"{receita}.txt"

        if nome_arquivo in pasta_receitas:
            favoritos.append(receita)
            print(f"'{receita}' foi adicionada aos favoritos.")
        else:
            print("Receita inválida. A receita não foi encontrada na pasta 'Receitas'.")

    def verfavoritos(favoritos):
        if favoritos:
            print("Suas receitas favoritas:")
            for idx, receita in enumerate(favoritos, 1):
                print(f"{idx}. {receita}")
        else:
            print("Você ainda não tem receitas favoritas.")

    
    def sugerirReceita():
        global pasta_receitas
        pasta_receitas = os.listdir("./Receitas")
        lista_receitas = []

        for receita in pasta_receitas:
            lista_receitas.append(os.path.splitext(receita)[0])
        
        sugestao = random.choice(lista_receitas)
        print(f"Receita sugerida: {sugestao}")

        return sugestao

    def atualizarReceita(receita_escolhida):
        ingredientes = ""
        modo_de_preparo = ""
        global pasta_receitas
        pasta_receitas = os.listdir("./Receitas")
        file = open(f"./Receitas/{receita_escolhida}.txt", "r")
        lines = file.readlines()
        for line in lines:
            if "Nome:" in line:
                nome = line.replace("Nome:", "").strip()
            if "Origem:" in line:
                origem = line.replace("Origem:", "").strip()
            if "Ingredientes:" in line:
                ingredientes = line.replace("Ingredientes:", "").strip()
            if "Modo de preparo:" in line:
                modo_de_preparo = line.replace("Modo de preparo:", "").strip()
        file.close()
        print("O que você deseja atualizar na receita?")
        print("1. Nome")
        print("2. Origem")
        print("3. Ingredientes")
        print("4. Modo de preparo")
        escolha = input("Escolha o número correspondente ao atributo que deseja atualizar: ")
        if escolha == "1":
            novonome = input("Digite o novo nome da receita: ").capitalize()
            os.rename(f'./Receitas/{receita_escolhida}.txt', f'./Receitas/{novonome}.txt')
            nome = novonome
            print(f"Nome atualizado para: {novonome}")
            file = open(f"./Receitas/{novonome}.txt", "w")
            file.write(f"Nome: {novonome}\n")
            file.write(f"Origem: {origem}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Modo de preparo: {modo_de_preparo}")
            file.close()
        elif escolha == "2":
            file = open(f"./Receitas/{nome}.txt", "w")
            novaorigem = input("Digite a nova origem da receita: ")
            print(f"Origem atualizada para: {novaorigem}")
            file.write(f"Nome: {nome}\n\n")
            file.write(f"Origem: {novaorigem}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Modo de preparo: {modo_de_preparo}\n")
            file.close()
        elif escolha == "3":
            file = open(f"./Receitas/{nome}.txt", "w")
            novoingrediente = input("Digite os novos ingredientes da receita (separados por vírgula): ")
            ingredientes = novoingrediente.split(", ")
            print(f"Ingrediente atualizado para: {novoingrediente}")
            file.write(f"Nome: {nome}\n\n")
            file.write(f"Origem: {origem}\n")
            file.write(f"Ingredientes: {novoingrediente}\n")
            file.write(f"Modo de preparo: {modo_de_preparo}\n")
            file.close()
        elif escolha == "4":
            file = open(f"./Receitas/{nome}.txt", "w")
            novopreparo = input("Digite o novo modo de preparo da receita: ")
            modo_de_preparo = novopreparo
            print(f"Modo de preparo atualizado para: {novopreparo}")
            file.write(f"Nome: {nome}\n\n")
            file.write(f"Origem: {origem}\n")
            file.write(f"Ingredientes: {ingredientes}\n")
            file.write(f"Modo de preparo: {novopreparo}\n")
            file.close()
        else:
            print("Escolha inválida.")

    def totalReceitas():
        print(f"\nNúmero total de receitas cadastradas: {len(os.listdir("Receitas"))}") 

    def paisMaisExplorado():
        global pasta_receitas
        pasta_receitas = os.listdir("./Receitas")

        paises = []

        for receita in pasta_receitas:
            nome_arquivo = f"{receita}"
            file = open(f"./Receitas/{nome_arquivo}", "r")
            lines = file.readlines()
            for line in lines:
                if "Origem:" in line:
                    paises.append(line[7:])

            file.close()

        max = 0

        for pais in paises:
            quant_pais = paises.count(pais)
            if quant_pais > max:
                max = quant_pais
                pais_mais_explorado = pais
            
        print(f"\nPaís mais explorado: {pais_mais_explorado}")  
