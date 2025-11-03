#THÉOPETSHOP 

usuarios = [['alice','alice@gmail.com', '12345678', 'A']]

while True:
    print('\nBem vindo ao Théopetshop\n')
    print('INÍCIO:\n') 
    print('1 - Cadastro')
    print('2 - Login') 
    print('3 - Sair\n')
    opcao = input('Digite a sua opção: ') 
    if(opcao == '3'):
        break
    elif(opcao == '1'):
            print('\nCADASTRAMENTO:\n') 
            tipo = input('Digite A para administrador ou C para cliente: ')
            while tipo not in ['A', 'C']:
                 print('Tipo inválido')
                 tipo = input('Digite A para administrador ou C para cliente: ') 

            if tipo == 'C':                
                 nome = input('\nDigite o nome do tutor(ra): ')
                 while len(nome) < 3:
                      print('Nome inválido, digite mais de 3 caracteres!')
                      nome = input('Digite seu nome: ') 

                 nome_pet = input('Digite o nome do seu pet: ')
                 while len(nome_pet) < 2:
                      print('Nome do pet inválido, digite mais de 2 caracteres!')
                      nome_pet = input('Digite o nome do seu pet: ')

                 email = input('Digite seu email: ')
                 while '@gmail.com' not in email:
                      print('Email inválido, tente novamente!') 
                      email = input('Digite seu email: ')

                 senha = input('Crie uma senha: ')
                 while len(senha) < 8:
                      print('Senha inválida, no mínimo 8 caracteres!')
                      senha = input('Crie uma senha: ')
            elif tipo == 'A':
                 nome = input('\nDigite seu nome: ')
                 while len(nome) < 3:
                      print('Nome inválido, digite mais de 3 caracteres!')
                      email = input('Digite seu email: ')

                 email = input('Digite seu email: ')    
                 while '@gmail.com' not in email:
                      print('Email inválido, tente novamente!') 
                      email = input('Digite seu email: ')

                 senha = input('Crie uma senha: ')
                 while len(senha) < 8:
                      print('Senha inválida, no mínimo 8 caracteres!')
                      senha = input('Crie uma senha: ')

            if tipo in ['A']:
                 usuarios.append([nome, email, senha, tipo])
                 print('\nCadastrado como administrador!') 
                 print('Agora faça seu login abaixo\n')

            elif tipo in ['C']:
                 usuarios.append([nome, email, senha, tipo]) 
                 print('\nCadastrado como cliente!\n')
                 print('Agora faça seu login abaixo\n') 
                                
    elif (opcao == '2'):
          print('\nLOGIN:')
          logando = True
          while logando:
            email = input('\nDigite seu email: ')
            senha = input('Digite sua senha: ')
            tipo = 'N'
          
            for a in usuarios:
                    if a[1] == email and a[2] == senha:
                         print(f'\nBem vindo(a) {a[0]} perfil adm!\n') 
                         tipo = a[3]
                         logando = False
            if logando == False and tipo == 'A':
                produtos = [
                    ['Ração de 1kg', 16, 15],
                    ['Petisco de 300g', 12, 40], 
                    ['Cama', 70, 10],
                    ['Shampoo', 30, 50] 
                ]                    
                serviços = [
                    ['Banho',35, [8,10]],
                    ['Banho e tosa',38, [8,10]],
                    ['Tosa higiênica',42, [14,15]],
                    ['Tosa completa',50, [14,15]] 
                ] 
                while True:
                    print('\nMENU DO ADMINISTRADOR: ')
                    print('\n1 - Cadastrar produtos')
                    print('2 - Cadastrar serviços')
                    print('3 - Voltar ao menu inícial\n')
                    opcao1 = input('Digite a sua opção: ')

                    if opcao1 == '1':
                         print('\nMENU PRODUTO: ')
                         print('\n1 - Cadastrar')
                         print('2 - Atualizar')
                         print('3 - Remover')
                         print('4 - Voltar')
                         opcao2 = input('\nDigite sua opção: ') 

                         if opcao2 == '1':
                              nomep = input('\nDigite o nome do produto: ')
                              quantidadep = input('Digite quantas unidades: ')
                              valorp = int(input('Digite o valor do produto: '))
                              produtos.append([nomep, valorp, quantidadep]) 
                                   
                         elif opcao2 == '2':
                              for n in range(len(produtos)):
                                   print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}') 
                              alterar = float(int(input('\nO que deseja mudar? '))) 

                              for n in range(len(produtos)):
                                   if alterar == produtos[n][0]:
                                        nomep = input('\nDigite o nome do produto: ') 
                                        produtos[n][0] = nomep 

                                   if alterar == produtos[n][1]:
                                        valorp = float(int(input('Digite o valor do produto: ')))
                                        produtos[n][1] = valorp

                                   if alterar == produtos[n][2]:
                                        quantidadep = int(input('Digite a quantidade do produto: '))
                                        produtos[n][2] = quantidadep 
          
                              for n in range(len(produtos)):
                                   print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}')                                            
                              
                         elif opcao2 == '3':
                              for n in range(len(produtos)):
                                   print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}') 
                              remover = input('\nDigite qual deseja remover: ')
                              produtos.remove(produtos[n])

                              for n in range(len(produtos)):
                                   print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}')  

                         elif opcao2 == '4':
                              break

            elif logando == False and tipo == 'C':
                 print(f'\nBem vindo(a) {a[0]}!\n')
                 while True:
                      print('\nMENU SERVIÇOS')
                      print('1 - Comprar produtos') 
                      print('2 - Agendar serviços')
                      print('3 - Avaliação de seviços')
                      print('4 - Voltar')
                      opcao3 = input('Digite a sua opção: ')

                      if opcao3 == '4':
                           break
                    #   if opcao3 == 1:








                    
                 break
            else:
                         print('\nDados incorretos, refaça o login\n')