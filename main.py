from classes import Receita

while True:
    opcao = int(input(f"""\nDigite a opção desejada:
[1] Adicionar
[2] Visualizar
[3] Atualizar
[4] Excluir
[6] Sugestão de receita
[7] Sair 
"""))

    if opcao == 5:
        break

    if opcao == 1:

        nomeInput = input("Digite o nome: ").capitalize()

        origemInput = input("Digite a origem: ").capitalize()
        
        ingredientesLista = input("Digite os ingredientes(separados por ; ): ").split(";")
        
        modo_de_preparoInput = input("Digite o modo de preparo: ")

        receita = Receita(nomeInput, origemInput, ingredientesLista, modo_de_preparoInput)

        # print(f"""Nome: {receita.nome}
        # Origem: {receita.origem}
        # Ingredientes: {receita.ingredientes}
        # Modo de preparo: {receita.modo_de_preparo}""")
        
        receita.adicionar(receita)

    elif opcao == 2:
        Receita.visualizarTodas()
        receita = input("\nDigite o nome da receita desejada: ").capitalize()
        Receita.buscarReceita(receita)

    elif opcao == 3:
        pass
    
    elif opcao == 6:
        while True:
            sugestao = Receita.sugerirReceita()

            op = int(input("\nDeseja ver a receita ou receber outra sugestão?\n[1] Ver receita\n[2] Receber outra sugestão\n"))

            if op == 1:
                Receita.buscarReceita(sugestao)
                break
            
            elif op == 2:
                continue
            
            else:
                print("Resposta inválida. Tente novamente")

