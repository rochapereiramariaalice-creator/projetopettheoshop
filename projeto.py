#THÉOPETSHOP 

adm = []
cliente = []

while True:
    print('\nBem vindo ao Théopetshop\n')
    print('MENU INICIAL:\n')
    print('1 - Cadastro')
    print('2 - Login') 
    print('3 - Sair\n')
    opcao = input('Digite a sua opção: ') 
    if(opcao == '3'):
        break
    elif(opcao == '1'):
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
                 adm.append([nome, email, senha, tipo])
                 print('\nCadastrado como administrador!') 
                 print('Agora faça seu login abaixo\n')

            elif tipo in ['C']:
                 cliente.append([nome_pet, nome, email, senha, tipo]) 
                 print('\nCadastrado como cliente!')
                 print('Agora faça seu login abaixo\n') 
                                
    elif (opcao == '2'):
            print('\nLOGIN:\n')
            tipo = input('Você é administrador(A) ou cliente(C)? ')

            if tipo in ['A']:
                 email = input('\nDigite seu email: ')
                 senha = input('Digite sua senha: ')

                 for a in adm:
                      if a[1] == email and a[2] == senha:
                           print(f'\nBem vindo(a) {a[0]} como administrador(ra)!\n')
                           break
                      else:
                           print('\nDados incorretos, refaça o login\n')

            elif tipo in ['C']:
                 nome_pet = input('\nDigite o nome de seu pet: ')
                 email = input('Digite seu email: ')
                 senha = input('Digite sua senha: ')

                 for c in cliente:
                      if c[0] == nome_pet and c[2] == email and c[3] == senha:
                           print(f'\nBem vindo(a) {c[1]} tutor(ra) de {c[0]}!\n') 
                           break
                      else:
                           print('\nDados incorretos, refaça o login\n')

            while tipo not in ['A', 'C']:
                 print('Tipo inválido')
                 tipo = input('Você é administrador(A) ou cliente(C)? ') 