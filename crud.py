'''
Implementar a opção 2 (procurar contato) da seguinte forma:
Ficar pedindo para digitar um nome até digitar um nome que existe;
mostrar então na tela TODOS os demais dados daquela pessoa, cujo
nome foi digitado.

Implementar a opção 3 (atualizar contato) da seguinte forma:
Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
endereco, ou telefone, ou celular, ou email, ou finalizar as
atualizações; ficar pedindo para digitar a opção até digitar uma
opção válida; realizar a atulização solicitada; até ser escolhida a
opção de finalizar as atualizações.

Implementar a opção 4 (listar contato) da seguinte forma:
Mostrar na tela os TODOS os dados de CADA um dos contatos presentes
na lista chamada agenda (eventualmente chamada de agd).

Entregar até domingo, dia 28 de abril de 2024.
'''
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('| Grupo: Bruno Martins, Victor Hugo Cruz, Pedro Henrique      |')
    print('|                                                             |')
    print('| Versão 2.0 de 06/maio/2024                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def novos_dados(elemento_novo, agd, posicao, opcao):
    agd[posicao][opcao] = elemento_novo
    print()
    print('Os dados atualizados de', agd[posicao][0], 'são:')
    print('Aniversario:',agd[posicao][1])
    print('Endereco:',agd[posicao][2])
    print('Telefone:',agd[posicao][3])
    print('Celular:',agd[posicao][4])
    print('e-mail:',agd[posicao][5])

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    PessoaEncontrada = False

    while not PessoaEncontrada:
        nome_procurado = input('Digite um nome já cadastrado: ')

        procurar_nome = ondeEsta(nome_procurado,agd)
        achou   = procurar_nome[0] 
        posicao = procurar_nome[1]

        if achou:
            print()
            print('Os dados atuais de', agd[posicao][0], 'são:')
            print('Aniversario:',agd[posicao][1])
            print('Endereco:',agd[posicao][2])
            print('Telefone:',agd[posicao][3])
            print('Celular:',agd[posicao][4])
            print('e-mail:',agd[posicao][5])
            
            PessoaEncontrada = True
        else:
            print("Essa pessoa não está na lista!")

    return posicao
        
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.

def atualizar (agd):
    menu_atualizar=['Atualizar Aniversário',\
    'Atualizar Endereço',\
    'Atualizar Teleone',\
    'Atualizar Celular',\
    'Atualizar e-mail',\
    'Finalizar Atualizações']
    opcao=777
    posicao = procurar(agd)
    print()
    print('Qual dado deseja atualizar?')
    while opcao!=6:
        finalizar = False
        while not finalizar:
        
            opcao = int(opcaoEscolhida(menu_atualizar))
            if opcao == 1:
                elemento_novo = input("Digite a nova data de aniversário: ")
                novos_dados(elemento_novo, agd, posicao, opcao)

            elif opcao == 2:
                elemento_novo = input('Digite o novo endereço: ')
                novos_dados(elemento_novo, agd, posicao, opcao)

            elif opcao == 3:
                elemento_novo = input('Digite o novo telefone: ')
                novos_dados(elemento_novo, agd, posicao, opcao)

            elif opcao == 4:
                elemento_novo = input("Digite o novo número de celular: ")
                novos_dados(elemento_novo, agd, posicao, opcao)

            elif opcao == 5:
                elemento_novo = input('Digite o novo e-mail: ')
                novos_dados(elemento_novo, agd, posicao, opcao)

            elif opcao == 6:
                print("Atualizações finalizadas!")
                finalizar = True
                break

            print()
            print("Deseja atualizar mais algum dado?")
           
    # Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
    # endereco, ou telefone, ou celular, ou email, ou finalizar as
    # atualizações; ficar pedindo para digitar a opção até digitar uma
    # opção válida; realizar a atulização solicitada; até ser escolhida a
    # opção de finalizar as atualizações.
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU

def listar (agd):
    if len(agd)==0:
        print('Não há contatos cadastrados!')
    else:
        agd.sort(key=lambda contato: contato[0].upper())
        print()
        print("Lista de Contatos:")
        print()
        posicao=0
        while posicao<len(agd):
            print("Nome:",agd[posicao][0])
            print("Aniversário:",agd[posicao][1])
            print("Endereço:",agd[posicao][2])
            print("Telefone:",agd[posicao][3])
            print("Celular:",agd[posicao][4])
            print("E-mail:",agd[posicao][5])
            print("--------------------")
            posicao+=1
    
    # implementar aqui a listagem de todos os dados de todos
    # os contatos cadastrados
    # printar aviso de que não há contatos cadastrados se
    # esse for o caso

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')

