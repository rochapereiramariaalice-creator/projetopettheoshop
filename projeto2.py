#PETTHEOSHOP 

import json
import os 
from datetime import datetime

comentarios = [{'nome': 'Alice', 'comentario': 'Que petshop legal'}]
lista_compras = [] 
usuarios = [
    {'nome': 'Alice', 'email': 'alice@gmail.com', 'senha': '12345678', 'tipo': 'A'}
]

produtos = [
    {'nome': 'Ração de 1kg', 'valor': 16.0, 'quantidade': 15},
    {'nome': 'Petisco de 300g', 'valor': 12.0, 'quantidade': 40}, 
    {'nome': 'Cama', 'valor': 70.0, 'quantidade': 10},
    {'nome': 'Shampoo', 'valor': 30.0, 'quantidade': 50}, 
    {'nome': 'Bolinha', 'valor': 10.0, 'quantidade': 40}
]
servicos = [
    {'nome': 'Banho', 'valor': 35.0, 'horarios': [8, 10]},
    {'nome': 'Banho e tosa', 'valor': 38.0, 'horarios': [8, 10]},
    {'nome': 'Tosa higiênica', 'valor': 42.0, 'horarios': [14, 15]},
    {'nome': 'Tosa completa', 'valor': 50.0, 'horarios': [14, 15]},
    {'nome': 'Banho completo', 'valor': 70.0, 'horarios': [16, 20]}
]

def carregar_dados_json(nome_arquivo, dados_padrao):
    try:
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r') as f:
                return json.load(f)
        else:
            return dados_padrao
    except Exception as e:
        print(f"Erro ao carregar {nome_arquivo}: {e}")
        return dados_padrao

def salvar_dados_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
        print(f"Dados de {nome_arquivo} salvos com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao salvar {nome_arquivo}: {e}")
        return False

def carregar_dados_do_backup():
    global usuarios, produtos, servicos
    print("\nIniciando Carregamento de Dados (Backup/Restauração)...")
    
    usuarios = carregar_dados_json('usuarios.json', usuarios)
    produtos = carregar_dados_json('produtos.json', produtos)
    servicos = carregar_dados_json('servicos.json', servicos)
    
    print("Carregamento de dados concluído.")

def gerar_relatorio_txt():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f'relatorio_theopetshop_{timestamp}.txt'
    
    try:
        with open(nome_arquivo, 'w') as f:
            f.write("="*50 + "\n")
            f.write("RELATÓRIO DE BACKUP DO THÉOPETSHOP\n")
            f.write(f"Data de Geração: {timestamp}\n")
            f.write("="*50 + "\n\n")

            f.write("LISTA DE USUÁRIOS\n")
            if usuarios:
                for u in usuarios:
                    f.write(f"Nome: {u['nome']} | Email: {u['email']} | Tipo: {'Administrador' if u['tipo'] == 'A' else 'Cliente'}\n")
            else:
                f.write("Nenhum usuário cadastrado.\n")
            f.write("-" * 40 + "\n\n")

            f.write("LISTA DE PRODUTOS\n")
            if produtos:
                for p in produtos:
                    f.write(f"Produto: {p['nome']} | Valor: R${p['valor']:.2f} | Estoque: {p['quantidade']}\n")
            else:
                f.write("Nenhum produto em estoque.\n")
            f.write("-" * 40 + "\n\n")

            f.write("SERVIÇOS DISPONÍVEIS\n")
            if servicos:
                for s in servicos:
                    horarios_str = ', '.join([f'{h}h' for h in s['horarios']])
                    f.write(f"Serviço: {s['nome']} | Valor: R${s['valor']:.2f} | Horários: [{horarios_str}]\n")
            else:
                f.write("Nenhum serviço cadastrado.\n")
            f.write("-" * 40 + "\n\n")
            
            f.write("HISTÓRICO DE COMPRAS E AGENDAMENTOS\n")
            if lista_compras:
                for tutor, produto, servico, horario, total in lista_compras:
                    prod_info = f"Produto: {produto}" if produto else "Produto: N/A"
                    serv_info = f"Serviço: {servico} ({horario}h)" if servico else "Serviço: N/A"
                    f.write(f"Tutor: {tutor} | {prod_info} | {serv_info} | Total: R${total:.2f}\n")
            else:
                f.write("Nenhuma compra ou agendamento registrado.\n")
            f.write("-" * 40 + "\n\n")

        print(f"Relatório de backup gerado com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"Erro ao gerar relatório TXT: {e}")

carregar_dados_do_backup()

while True:
    print('\nBem vindo ao Théopetshop\n')
    print('INÍCIO:\n') 
    print('1 - Cadastro')
    print('2 - Login') 
    print('3 - Sair')
    print('4 - Avaliações do PETSHOP\n')
    opcao = input('Digite a sua opção: ') 
    
    if(opcao == '3'):
        break
    
    if opcao == '4':
        if len(comentarios) == 0:
            print('\nNenhuma avaliação no PETSHOP.\n') 
        else:
            print('\nAvaliações do PETSHOP:\n')
            for c in comentarios:
                print(f'Nome: {c["nome"]} | Comentário: {c["comentario"]}') 
    
    elif(opcao == '1'):
        print('\nCADASTRAMENTO:\n') 
        tipo = input('Digite A para administrador ou C para cliente: ')
        while tipo not in ['A', 'C']:
            print('Tipo inválido')
            tipo = input('Digite A para administrador ou C para cliente: ') 
    
        nome = input('\nDigite o nome: ')
        email = input('Digite seu email: ')
        senha = input('Crie uma senha: ')
          
        novo_usuario = {
              'nome': nome,
              'email': email,
              'senha': senha,
              'tipo': tipo
          }
          
        usuarios.append(novo_usuario)
        print(f'\nCadastrado como {"administrador" if tipo == "A" else "cliente"}!\n')
        salvar_dados_json('usuarios.json', usuarios)
              
    elif (opcao == '2'):
        print('\nLOGIN:')
        logando = True
        while logando:
            email = input('\nDigite seu email: ')
            senha = input('Digite sua senha: ')
            usuario_logado = None
             
            for u in usuarios:
                if u['email'] == email and u['senha'] == senha:
                    usuario_logado = u
                    logando = False
                    break

            if usuario_logado and usuario_logado['tipo'] == 'A':
                print(f'\nBem vindo(a) {usuario_logado["nome"]}! (ADMINISTRADOR)\n') 
                 
                while True:
                    print('\nMENU DO ADMINISTRADOR: ')
                    print('\n1 - Gerenciar produtos')
                    print('2 - Gerenciar serviços')
                    print('3 - Controle de produtos (Estoque)') 
                    print('4 - Controle de horários') 
                    print('5 - Opções de Backup e Relatório')
                    print('6 - Voltar ao menu inicial\n')
                    opcao1 = input('Digite sua opção: ')
                    
                    if opcao1 == '5':
                        print('\nOPÇÕES DE BACKUP E RELATÓRIO')
                        print('1 - Salvar Dados Atuais (Backup em json)')
                        print('2 - Gerar Relatório Completo em txt')
                        print('3 - Voltar para o menu administrador')
                        opcao_backup = input('\nDigite sua opção: ')
                         
                        if opcao_backup == '1':
                            print("\nSalvando os dados atuais...")
                            salvar_dados_json('usuarios.json', usuarios)
                            salvar_dados_json('produtos.json', produtos)
                            salvar_dados_json('servicos.json', servicos)

                        elif opcao_backup == '2':
                            gerar_relatorio_txt()

                        elif opcao_backup == '3':
                            continue

                        else:
                            print("Opção inválida.")
                             
                    elif opcao1 == '1':
                        print('\nMENU PRODUTO: ')
                        print('\n1 - Cadastrar')
                        print('2 - Atualizar')
                        print('3 - Remover') 
                        print('4 - Voltar para o menu administrador')
                        opcao2 = input('\nDigite sua opção: ') 
    
                        if opcao2 == '1':
                            nomep = input('\nDigite o nome do produto: ')
                            quantidadep = int(input('Digite quantas unidades: '))
                            valorp = float(input('Digite o valor do produto: '))
                            novo_produto = {'nome': nomep, 'valor': valorp, 'quantidade': quantidadep}
                            produtos.append(novo_produto) 
                            salvar_dados_json('produtos.json', produtos)
                                  
                        elif opcao2 == '2':
                            for indice, p in enumerate(produtos):
                                print(f'Código: {indice} | Produto: {p["nome"]} | Valor: R${p["valor"]:.2f} | Quantidade: {p["quantidade"]}')

                            indice = int(input('Digite o indice que deseja alterar: '))
                            if 0 <= indice < len(produtos):
                                nomep = input("Digite o novo nome: ")
                                valorp = float(input('Digite o novo valor: '))
                                quantidadep = int(input('Digite a nova quantidade: '))
                                
                                produtos[indice]['nome'] = nomep
                                produtos[indice]['valor'] = valorp
                                produtos[indice]['quantidade'] = quantidadep
                                
                                salvar_dados_json('produtos.json', produtos)
                            else:
                                print('Índice inválido.')

                            for p in produtos:
                                print(f'Produto: {p["nome"]} | Valor: {p["valor"]:.2f} | Quantidade: {p["quantidade"]}')
                            
                        elif opcao2 == '3':
                            for i, p in enumerate(produtos):
                                print(f'Código: {i} | Produto: {p["nome"]} | Valor: R${p["valor"]:.2f} | Quantidade: {p["quantidade"]}')

                            indice = int(input('\nDigite o indice para remover: '))
                            if 0 <= indice < len(produtos):
                                produtos.pop(indice)
                                salvar_dados_json('produtos.json', produtos)
                            else:
                                print('Índice inválido.')
                            
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
                            valorservico = float(input('Digite o valor: '))
                            horario_count = int(input('Digite quantos horários você deseja cadastrar: '))
                            horarios = []
                            for i in range(horario_count):
                                horarios.append(int(input(f'Qual horário deseja adicionar ({i+1}/{horario_count}): ')))
                            
                            novo_servico = {'nome': nomeservico, 'valor': valorservico, 'horarios': horarios}
                            servicos.append(novo_servico)
                            salvar_dados_json('servicos.json', servicos)
                            
                        elif opcao4 == '2':
                            for s_idx, s in enumerate(servicos):
                                horarios_str = ', '.join([f'{h}h' for h in s['horarios']])
                                print(f'Código {s_idx} | Serviço: {s["nome"]} | Valor: R${s["valor"]:.2f} | Horários: {horarios_str}') 
                                
                            indice = int(input('Digite o indice que deseja alterar: '))
                            if 0 <= indice < len(servicos):
                                nomeservico = input("Digite o novo nome do serviço: ")
                                valorservico = float(input('Digite o novo valor: '))
                                horario_count = int(input('Digite quantos horários você deseja adicionar: '))
                                horarios = []
                                for i in range(horario_count):
                                    horarios.append(int(input(f'Qual horário deseja adicionar ({i+1}/{horario_count}): ')))
                                    
                                servicos[indice]['nome'] = nomeservico
                                servicos[indice]['valor'] = valorservico
                                servicos[indice]['horarios'] = horarios
                                
                                salvar_dados_json('servicos.json', servicos)
                            else:
                                print('Índice inválido.')

                        elif opcao4 == '3':
                            for i, s in enumerate(servicos):
                                print(f'Código: {i} | Serviço: {s["nome"]} | Valor: R${s["valor"]:.2f} | Horário: {s["horarios"]}h') 

                            indices = int(input('\nDigite o indice para remover: '))
                            if 0 <= indices < len(servicos):
                                servicos.pop(indices)
                                salvar_dados_json('servicos.json', servicos)
                            else:
                                print('Índice inválido.')
                        
                    elif opcao1 == '3':
                        print('\nESTOQUE:')
                        for p in produtos:
                            print(f'Produto: {p["nome"]} | Valor: R${p["valor"]:.2f} | Quantidade: {p["quantidade"]}') 

                    elif opcao1 == '4':
                        print('LISTA DE HORÁRIOS:')
                        for s in servicos:
                            horarios_str = ', '.join([f'{h}h' for h in s['horarios']])
                            print(f'Serviço: {s["nome"]} | Valor: R${s["valor"]:.2f} | Horários: {horarios_str}') 

                    elif opcao1 == '6':
                        break
                    else:
                        print("Opção inválida.")

            elif usuario_logado and usuario_logado['tipo'] == 'C':
                print(f'\nBem vindo(a) {usuario_logado["nome"]}! (CLIENTE)\n')

                while True:
                    print('\nMENU CLIENTE:') 
                    print('\n1 - Agendamento e compra')
                    print('2 - Avaliar PETSHOP')
                    print('3 - Voltar para o menu inicial')
                    opcao3 = input('\nDigite a sua opção: ')

                    if opcao3 == '2':
                        print('Deixe seu comentario para o THÉOPETSHOP abaixo:\n')
                        comentario = input('Deixe sua avaliação: ')
                        comentarios.append({'nome': usuario_logado['nome'], 'comentario': comentario}) 
                        print('\nObrigado(a) pela avaliação!\n')

                    if opcao3 == '3':
                        break 
                        
                    if opcao3 == '1':
                        total_compra = 0
                        total_servico = 0
                        produto_comprado = ''
                        servico_agendado = ''
                        horario_escolhido = 0 
                        
                        print('\nProdutos disponíveis: ')
                        for n, p in enumerate(produtos):
                            print(f'Código: {n} | Produto: {p["nome"]} | Valor: R${p["valor"]:.2f} | Quantidade: {p["quantidade"]}')

                        opcao5 = input('\nDigite o código do produto que deseja comprar (ou -1 para pular): ')
                        if opcao5.isdigit() or opcao5 == '-1':
                            opcao5 = int(opcao5)

                            if opcao5 != -1:
                                if 0 <= opcao5 < len(produtos):
                                    p_selecionado = produtos[opcao5]
                                    try:
                                        quantidade = int(input('Quantas unidades deseja comprar: '))

                                        if quantidade > p_selecionado['quantidade']:
                                            print(f'Valor inválido, nós so temos {p_selecionado["quantidade"]} unidades disponíveis.')

                                        elif quantidade > 0:
                                            total_compra = p_selecionado['valor'] * quantidade
                                            p_selecionado['quantidade'] -= quantidade 
                                            produto_comprado = p_selecionado['nome'] 
                                            salvar_dados_json('produtos.json', produtos)
                                            print(f'\nCompra de {quantidade}x {p_selecionado["nome"]} adicionada. Total: R${total_compra:.2f}')

                                        else:
                                            print("Quantidade deve ser maior que zero.")
                                    except ValueError:
                                        print("Quantidade inválida.")

                                else:
                                    print('Código de produto inválido!')
                        else:
                            print("Opção inválida para produto.")
                            
                        print('\nServiços disponíveis: ') 
                        for s_idx, s in enumerate(servicos):
                            horarios_str = ', '.join([f'{h}h' for h in s['horarios']])
                            print(f'Código: {s_idx} | Serviço: {s["nome"]} | Valor: R${s["valor"]:.2f} | Horários disponíveis: {horarios_str}')

                        opcao6 = input('\nDigite o código do serviço que deseja agendar (ou -1 para pular): ')
                        if opcao6.isdigit() or opcao6 == '-1':
                            opcao6 = int(opcao6)

                            if opcao6 != -1:
                                if 0 <= opcao6 < len(servicos):
                                    s_selecionado = servicos[opcao6]
                                    try:
                                        horario = int(input('Digite o horário desejado: '))
                                        if horario not in s_selecionado['horarios']:
                                            print('Horário indisponível!')

                                        else:
                                            total_servico = s_selecionado['valor'] 
                                            servico_agendado = s_selecionado['nome'] 
                                            horario_escolhido = horario
                                            s_selecionado['horarios'].remove(horario)
                                            salvar_dados_json('servicos.json', servicos) 
                                            print(f'\nServiço {s_selecionado["nome"]} agendado para {horario}h por R${total_servico:.2f}') 
                                    except ValueError:
                                        print("Horário inválido.")
                                else:
                                    print('Código de serviço inválido!')

                        else:
                            print("Opção inválida para serviço.")
                            
                        total_geral = total_compra + total_servico

                        if total_geral > 100:
                            desconto = total_geral * 0.05
                            total_geral -= desconto
                            print(f'\nVocê ganhou 5% de desconto (R${desconto:.2f}), pois seu valor final foi mais de 100 reais.')

                        if total_compra > 0 or total_servico > 0:
                            print(f'\nValor total a pagar: R${total_geral:.2f}')
                            lista_compras.append([usuario_logado['nome'], produto_comprado, servico_agendado, horario_escolhido, total_geral])

                        else:
                            print('\nNenhuma compra ou agendamento realizado.') 
                                                                
                    break 

            else:
                print('\nDados incorretos, refaça o login\n')