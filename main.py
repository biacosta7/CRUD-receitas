from classes import Receita

while True:
    try:
        opcao = int(input(f"""\nDigite a opção desejada:
    [1] Adicionar
    [2] Visualizar
    [3] Atualizar
    [4] Excluir
    [5] Filtrar por país
    [6] Sugestão de receita 
    [7] Ver estatísticas 
    [8] Sair

    """))

        if opcao == 1:

            nomeInput = input("Digite o nome: ").capitalize()

            origemInput = input("Digite a origem: ").capitalize()
            
            ingredientesLista = input("Digite os ingredientes(separados por ; ): ").split(";")
            
            modo_de_preparoInput = input("Digite o modo de preparo: ")

            receita = Receita(nomeInput, origemInput, ingredientesLista, modo_de_preparoInput)
            
            receita.adicionar(receita)

        elif opcao == 2:
            Receita.visualizarTodas()
            receita = input("\nDigite o nome da receita desejada: ").capitalize()
            Receita.buscarReceita(receita)

        elif opcao == 3:
            Receita.visualizarTodas()
            while True:
                try:
                    nome_receita = input("Digite o nome da receita que deseja atualizar: ").capitalize()
                    Receita.atualizarReceita(nome_receita)
                    break
                except ValueError:
                    print("Valor inválido. Tente novamente.")

        elif opcao == 4:
            Receita.visualizarTodas()
            excluir = input("\nDigite o nome da receita que deseja excluir: ").capitalize()
            Receita.exclusao(excluir)
            print("Receita excluída com sucesso.")

        elif opcao == 5:
            while True:
                try:
                    nacionalidade = input("Insira de qual país você deseja visualizar as receitas: ").capitalize()
                    Receita.filtrarPais(nacionalidade)
                    break
                except ValueError:
                    print("Valor inválido. Tente novamente.")

        elif opcao == 6:
            while True:
                sugestao = Receita.sugerirReceita()

                try:
                    op = int(input("\nDeseja ver a receita ou receber outra sugestão?\n[1] Ver receita\n[2] Receber outra sugestão\n"))

                    if op == 1:
                        Receita.buscarReceita(sugestao)
                        break
                    
                    elif op == 2:
                        continue
                    
                    else:
                        print("Resposta inválida. Tente novamente")
        
                except ValueError:
                    print("Valor inválido. Tente novamente.")


        elif opcao == 7:
            op = int(input(f"""Digite a opção que deseja ver: 
    [1] Número total de receitas cadastradas
    [2] País mais explorado 
    """))

            if op == 1:
                Receita.totalReceitas()

            elif op == 2:
                Receita.paisMaisExplorado()

        elif opcao == 8:
            break

    except ValueError:
        print("Valor inválido. Tente novamente.")
