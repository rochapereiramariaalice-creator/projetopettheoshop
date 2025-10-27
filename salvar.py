#THÉOPETSHOP 

adm = []
cliente = []

while True:
    print('Bem vindo ao Théopetshop!\n')
    print('MENU INICIAL:\n')
    print('1 - Cadastro')
    print('2 - Login') 
    print('3 - Sair\n')
    opcao = input('Digite a sua opção: ') 
    if(opcao == '3'):
        break
    elif(opcao == '1'):
            nome = input('\nDigite o nome do tutor(ra): ')
            while len(nome) < 3:
                 print('Nome incorreto, digite mais de 3 caracteres')
                 nome = input('Digite seu nome: ') 

            nome_pet = input('Digite o nome do seu pet: ')
            while len(nome_pet) < 2:
                 print('Nome do pet incorreto, digite mais de 2 caracteres')
                 nome_pet = input('Digite o nome do seu pet: ')

            email = input('Digite seu email: ')
            while '@gmail.com' not in email:
                print('Email inválido, tente novamente') 
                email = input('Digite seu email: ')

            senha = input('Crie uma senha: ')
            while len(senha) < 8:
                 print('Senha incorreta, no mínimo 8 caracteres')
                 senha = input('Crie uma senha: ')

            tipo = input('Digite A para administrador ou C para cliente: ')
            while tipo not in ['A', 'C']:
                 print('Opção inválida')
                 tipo = input('Digite A para administrador ou C para cliente: ')
            if tipo in ['A']:
                 adm.append([nome, email, senha, tipo])
                 print('Cadastrado como administrador\n')
            else:
                 cliente.append([nome_pet, nome, email, senha, tipo])
                 print('Cadastrado como cliente\n')
                                
    elif (opcao == '2'):
            print('\nLOGIN:\n')
            tipo = input('Você é administrador ou cliente? ')

            if tipo in ['A']:
                 email = input ('Digite seu email: ')
                 senha = input ('Digite sua senha: ')

                 for n in adm:
                      if n[1] == email and n[2] == senha:
                           print(f'Bem vindo(a) {n[0]}\n')
                           break
                      else:
                           print('Email ou senha incorretos\n')