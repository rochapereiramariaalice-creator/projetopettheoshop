#THÉOPETSHOP 

usuarios = [['alice','alice@gmail.com', '12345678', 'A']]
produtos = [
     ['Ração de 1kg', 16.0, 15],
     ['Petisco de 300g', 12, 40], 
     ['Cama', 70.0, 10],
     ['Shampoo', 30.0, 50] 
]                    
servicos = [
     ['Banho', 35.0, [8,10]],
     ['Banho e tosa', 38.0, [8,10]],
     ['Tosa higiênica', 42.0, [14,15]],
     ['Tosa completa', 50.0, [14,15]] 
] 

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
                         tipo = a[3]
                         logando = False
               if logando == False and tipo == 'A':
                    print(f'\nBem vindo(a) {a[0]}!\n')
                   
                    while True:
                         print('\nMENU DO ADMINISTRADOR: ')
                         print('\n1 - Cadastrar produtos')
                         print('2 - Cadastrar serviços')
                         print('3 - Controle de produtos')
                         print('4 - Controle de horários') 
                         print('5 - Voltar ao menu inicial\n')
                         opcao1 = input('Digite a sua opção: ')

                         if opcao1 == '1':
                              print('\nMENU PRODUTO: ')
                              print('\n1 - Cadastrar')
                              print('2 - Atualizar')
                              print('3 - Remover') 
                              print('4 - Voltar para o menu administrador')
                              opcao2 = input('\nDigite sua opção: ') 

                              if opcao2 == '1':
                                   nomep = input('\nDigite o nome do produto: ')
                                   quantidadep = input('Digite quantas unidades: ')
                                   valorp = int(input('Digite o valor do produto: '))
                                   produtos.append([nomep, valorp, quantidadep]) 
                                        
                              elif opcao2 == '2':
                                   for indice in range(len(produtos)):
                                        print(f'Código: {indice} | Produto: {produtos[indice][0]} | Valor: {produtos[indice][1]} | Quantidade: {produtos[indice][2]}')

                                   indice = int(input('Digite o indice que deseja alterar: '))
                                   while indice < 0 or indice >= len(produtos):
                                        print('Inválido')
                                   indice = int (input('Digite o indice que deseja alterar: '))

                                   nomep = input("Digite o novo nome: ")
                                   valorp = input('Digite o novo valor: ')
                                   quantidadep = input('Digite a nova quantidade: ')
                                   novaSublista = [nomep, valorp, quantidadep]
                                   produtos[indice] = novaSublista
               
                                   for n in range(len(produtos)):
                                        print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}')                                            
                                   
                              elif opcao2 == '3':
                                   for i in range(len(produtos)):
                                        print(f'Código: {i} | Produto: {produtos[i][0]} | Valor: {produtos[i][1]} | Quantidade: {produtos[i][2]}')

                                   indice = int(input('\nDigite o indice para remover: '))
                                   produtos.remove(produtos[indice])

                                   for i in range(len(produtos)):
                                        print(f'Código: {i} | Produto: {produtos[i][0]} | Valor: {produtos[i][1]} | Quantidade: {produtos[i][2]}') 
                                   
                              elif opcao2 == '4':
                                   break

                         elif opcao1 == '2':
                              print('\nMENU SERVIÇOS: ')
                              print('\n1 - Cadastrar')
                              print('2 - Atualizar')
                              print('3 - Remover')
                              print('4 - Voltar para o menu administrador') 
                              opcao4 = input ('Digite a opção desejada: ')

                              if opcao4 == '4':
                                   break

                              elif opcao4 == '1':
                                   nomeservico = input('\nDigite o nome do serviço: ')
                                   valorservico = input('Digite o valor: ')
                                   horario = input('Digite a hora: ')
                                   servicos.append([nomeservico, valorservico, horario]) 

                              elif opcao4 == '2':
                                   for s in range(len(servicos)):
                                        print(f'Código {s} | Serviço: {servicos[s][0]} | Valor: {servicos[s][1]}')
                                        for s in servicos[s][2]:
                                             print(f'| Horário: {s}') 
                                   

                                   indice = int(input('Digite o indice que deseja alterar: '))
                                   while indice < 0 or indice >= len(servicos):
                                        print('Inválido')
                                        indice = int(input('Digite o indice que deseja alterar: '))

                                   nomeservico = input("Digite o novo nome do serviço: ")
                                   valorservico = float(input('Digite o novo valor: '))
                                   horario = int(input('Digite quantos horáios você deseja adicionar: '))
                                   horario = []
                                   novaSublista = [nomeservico, valorservico, horario]
                                   servicos[indice] = novaSublista

                              elif opcao4 == '3':
                                   for i in range(len(servicos)):
                                        print(f'Código: {i} | Serviço: {servicos[i][0]} | Valor: {servicos[i][1]} | Horário: {servicos[i][2]}')

                                   indices = int(input('\nDigite o indice para remover: '))
                                   servicos.remove(servicos[indices])

                                   for i in range(len(servicos)):
                                        print(f'Código: {i} | Serviço: {servicos[i][0]} | Valor: {servicos[i][1]} | Horário: {servicos[i][2]}')
                         
                         elif opcao1 == '3':
                              print('\nESTOQUE:')
                              for n in range(len(produtos)):
                                   print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}') 

                         elif opcao1 == '4':
                              break

                         elif opcao1 == '5':
                              break

               elif logando == False and tipo == 'C':
                    print(f'\nBem vindo(a) {a[0]}!\n')
                    while True:
                         print('\nMENU SERVIÇOS:') 
                         print('\n1 - Comprar produtos') 
                         print('2 - Agendar serviços')
                         print('3 - Avaliação de seviços')
                         print('4 - Voltar para o menu inicial')
                         opcao3 = input('Digite a sua opção: ')

                         if opcao3 == '4':
                              break 

                         if opcao3 == '1':
                              print('\nProdutos disponíveis: ')

                              for n in range(len(produtos)):
                                   print(f'Produto: {produtos[n][0]} | Valor: {produtos[n][1]} | Quantidade: {produtos[n][2]}')

                    







                    
                    break
               else:
                   print('\nDados incorretos, refaça o login\n') 