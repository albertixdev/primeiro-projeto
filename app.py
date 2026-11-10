import os

restaurantes = [{'nome':'praça', 'categoria':'Japonesa', 'ativo':False}, {'nome':'Pizza suprema', 'categoria':'Pizza', 'ativo':True}, {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    '''exibe o nome do programa criado'''
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    '''exibe as opções q o nosso programa oferece'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''finaliza o programa quando a opção 4 é assioanada'''
    exibir_subtitulo('Finalizando programa')

def voltar_ao_menu_principal():
    '''depois de cada utilização das opcões elas voltam para o menu de exibir opcões'''
    input('\naperte uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''quando o cliente n escolhe um dos numeros'''
    print('opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''essa função exibe o subtitulo em todos outros codigos'''
    os.system('cls')
    linha = '*' * (len(texto))
    print('|' + linha + '|')
    print('|' + texto + '|')
    print('|' + linha + '|')
    print()

def cadastrar_novo_restaurante():
    '''função responsavel por cadastrar restaurantes'''
    exibir_subtitulo('cadastro de novos restaurantes')
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'qual a categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''funçao responsavel por listar os restaurantes'''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | ativo')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''função responsavel por ativer e desativar os restaurantes'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcoes():
    '''base do codigo, onde direcionamos cada opção'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''função que organiza a ordem do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()

