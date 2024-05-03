from classes import Receita

while True:
    opcao = int(input(f"""\nDigite a opção desejada:
[1] Adicionar
[2] Visualizar
[3] Atualizar
[4] Excluir
[5] Sair 
"""))

    if opcao == 5:
        break

    if opcao == 1:

        nomeInput = input("Digite o nome: ").capitalize()

        origemInput = input("Digite a origem: ").capitalize()
        
        ingredientesInput = input("Digite os ingredientes(separados por ; ): ")
        ingredientesLista = ingredientesInput.split("; ")
        
        modo_de_preparoInput = input("Digite o modo de preparo: ")

        receita = Receita(nomeInput, origemInput, ingredientesLista, modo_de_preparoInput)

        print(f"""Nome: {receita.nome}
        Origem: {receita.origem}
        Ingredientes: {receita.ingredientes}
        Modo de preparo: {receita.modo_de_preparo}""")
        
        receita.adicionar(receita)

    elif opcao == 2:
        pass
    
    elif opcao == 3:
        pass
    
    elif opcao == 4:
        pass



