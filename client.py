# Desenvolvido por: Rafael Duarte

import socket

comando = []
placarJog1 = []
placarJog2 = []

#funcao para separar o comando e numero de hash atribuido ao client pelo server
def separaComandoComHash(mensagemRecebida):
    comandoSep = mensagemRecebida[0:7]
    hash = mensagemRecebida[7:]
    return comandoSep, hash

#funcao apenas para separar o comando dos atributos
def separaComando(mensagemRecebida):
    comandoSep = mensagemRecebida[0:7]
    return comandoSep

#funcao para responder a solicitação de classe feita pelo server
def chooseTime(client):
    while 1:
        selectClass = int(input('\nSeleção de Time\n\t1.Brasil \n\t2.Real Madri \nDigite sua escolha: '))
        if(selectClass == 1):
            comando = 'SELTIME1'
            break
        elif(selectClass == 2):
            comando = 'SELTIME2'
            break
        else:
            print('Time inválido')

    message = comando
    EncodeMessage = message.encode()
    client.send(EncodeMessage)

#funcao para responder a solicitação de ataque feita pelo server
def retornaATK(client):
    while 1:
        selectAtk = int(input('\nDirecao do Chute: 1 a 6\nDigite sua escolha: '))
        if(selectAtk == 1):
            comando = 'RETCHUT1'
            break
        elif(selectAtk == 2):
            comando = 'RETCHUT2'
            break
        elif(selectAtk == 3):
            comando = 'RETCHUT3'
            break
        elif(selectAtk == 4):
            comando = 'RETCHUT4'
            break
        elif(selectAtk == 5):
            comando = 'RETCHUT5'
            break
        elif(selectAtk == 6):
            comando = 'RETCHUT6'
            break
        else:
            print('Direcao inválida')

    message = comando
    EncodeMessage = message.encode()
    client.send(EncodeMessage)

#funcao para responder a solicitação de defesa feita pelo server
def retornaDEF(client):
    while 1:
        selectDEF = int(input('\nDirecao da defesa: 1 a 6\nDigite a escolha: '))
        if(selectDEF == 1):
            comando = 'DEFENDR1'
            break
        elif(selectDEF == 2):
            comando = 'DEFENDR2'
            break
        elif(selectDEF == 3):
            comando = 'DEFENDR3'
            break
        elif(selectDEF == 4):
            comando = 'DEFENDR4'
            break
        elif(selectDEF == 5):
            comando = 'DEFENDR5'
            break
        elif(selectDEF == 6):
            comando = 'DEFENDR6'
            break
        else:
            print('Direcao de defesa inválida')

    message = comando
    EncodeMessage = message.encode()
    client.send(EncodeMessage)

def incPlacar(tentativa, quemJoga):
    if(quemJoga == 1):
        if(tentativa == 2):
            placarJog1.append(" O ")

        else:
            placarJog1.append(" X ")

    else:
        if(tentativa == 2):
            placarJog2.append(" O ")

        else:
            placarJog2.append(" X ")


#funcao para atualizar os dados e ações do turno após o fim do mesmo
def atualizacaoTurno(comandoCompletoServidor, hash):
    posicaoVetor = 0
    tentativa = 0
    hash = int(hash)
    quemJoga = int(comandoCompletoServidor[7])
    print()
    print("Comando Completo: ", comandoCompletoServidor)
    print()
    if(hash == 1):
        if(quemJoga == 1):
            tentativa = int(comandoCompletoServidor[8])
            placar1 = int(comandoCompletoServidor[9])
            placar2 = int(comandoCompletoServidor[11])
            incPlacar(tentativa, quemJoga)
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            if(tentativa == 2):
                print("GOL !!!")
            elif(tentativa == 1):
                print("CHUTE PARA FORA !!!")
            elif(tentativa == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()
            print('\n\t\t ##### FIM DE TURNO #####\n')
        else:
            tentativa = int(comandoCompletoServidor[8])
            placar1 = int(comandoCompletoServidor[9])
            placar2 = int(comandoCompletoServidor[11])
            incPlacar(tentativa, quemJoga)
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            if(tentativa == 2):
                print("GOL !!!")
            elif(tentativa == 1):
                print("CHUTE PARA FORA !!!")
            elif(tentativa == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()

            print('\n\t\t ##### FIM DE TURNO #####\n')
    elif(hash == 2):
        if(quemJoga == 1):
            tentativa = int(comandoCompletoServidor[8])
            placar1 = int(comandoCompletoServidor[9])
            placar2 = int(comandoCompletoServidor[11])
            incPlacar(tentativa, quemJoga)
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            if(tentativa == 2):
                print("GOL !!!")
            elif(tentativa == 1):
                print("CHUTE PARA FORA !!!")
            elif(tentativa == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()

            print('\n\t\t ##### FIM DE TURNO #####\n')
        else:
            tentativa = int(comandoCompletoServidor[8])
            placar1 = int(comandoCompletoServidor[9])
            placar2 = int(comandoCompletoServidor[11])
            incPlacar(tentativa, quemJoga)
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            if(tentativa == 2):
                print("GOL !!!")
            elif(tentativa == 1):
                print("CHUTE PARA FORA !!!")
            elif(tentativa == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()

            print('\n\t\t ##### FIM DE TURNO #####\n')

#funcao para atualizar os dados e ações do turno após o fim do mesmo e anunciar o fim do jogo mostrando o vencedor
def gameOverATT(comandoCompletoServidor, hash):

    quemJoga = 0
    flagCampeao = 0

    hash = int(hash)
    quemJoga = int(comandoCompletoServidor[7])
    placar1 = int(comandoCompletoServidor[9])
    placar2 = int(comandoCompletoServidor[11])
    flagCampeao = int(comandoCompletoServidor[12])
    if(hash == 1):
        if(quemJoga == 1):
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            aux1 = int(comandoCompletoServidor[8])
            if(aux1 == 2):
                print("GOL !!!")
            elif(aux1 == 1):
                print("CHUTE PARA FORA !!!")
            elif(aux1 == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()
            print('\n\t\t ##### FIM DE JOGO #####\n')
            if(flagCampeao == 1):
                print('\n\n########################################################################')
                print('VOCE GANHOU !!!')
            else:
                print('\n\n########################################################################')
                print('VOCE PERDEU !!!')
        else:
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            aux1 = int(comandoCompletoServidor[8])
            if(aux1 == 2):
                print("GOL !!!")
            elif(aux1 == 1):
                print("CHUTE PARA FORA !!!")
            elif(aux1 == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()

            print('\n\t\t ##### FIM DE JOGO #####\n')
            if(flagCampeao == 1):
                print('\n\n########################################################################')
                print('VOCE GANHOU !!!')
            else:
                print('\n\n########################################################################')
                print('VOCE PERDEU !!!')
    elif(hash == 2):
        if(quemJoga == 1):
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            aux1 = int(comandoCompletoServidor[8])
            if(aux1 == 2):
                print("GOL !!!")
            elif(aux1 == 1):
                print("CHUTE PARA FORA !!!")
            elif(aux1 == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()

            print('\n\t\t ##### FIM DE JOGO #####\n')
            if(flagCampeao == 2):
                print('\n\n########################################################################')
                print('VOCE GANHOU !!!')
            else:
                print('\n\n########################################################################')
                print('VOCE PERDEU !!!')
        else:
            print('\n\t\t ##### ATUALIZAÇÃO #####\n')
            print('Placar: ')
            print('Jogador 1: ', placar1, ' - ', placarJog1)
            print('Jogador 2: ', placar2, ' - ', placarJog2)
            print()
            
            aux1 = int(comandoCompletoServidor[8])
            if(aux1 == 2):
                print("GOL !!!")
            elif(aux1 == 1):
                print("CHUTE PARA FORA !!!")
            elif(aux1 == 0):
                print("DEFESA DO GOLEIRO !!!")

            print()

            print('\n\t\t ##### FIM DE JOGO #####\n')
            if(flagCampeao == 2):
                print('\n\n########################################################################')
                print('VOCE GANHOU !!!')
            else:
                print('\n\n########################################################################')
                print('VOCE PERDEU !!!')

# Desenho dos Logos apenas para Ilustrar
def imprimeTimes():
    print("   ## 		 ")
    print("  ### 		 ")
    print("   ##       ##")
    print("   ## 		 ")
    print("   ## 		 ")
    print("   ##       ##")
    print(" ###### 		 ")

    print("                       ╫")
    print("                   '%@@╣▓@@*")
    print("                     j╣╬╣▒")
    print("                     ╜   ╙")
    print("         ╓Mⁿ▄                  ,M""ª▄")
    print("       ▄╜▀▄▄▄▄▄▄▓▓▓▓▓▓▓▓▓▓▓▓▄▄▄▓▄▄▄▄,`Ñ╖")
    print("       ▓h████▓▓▓▓▓████▓▓▓▓▓████▓▓▓▓▓██▄^▓")
    print("      ╙W▄⌐███▓▓▓▓▓████▓▓▓▓▓████▓▓▓▓▓████ ▀┐")
    print("         ▐∩██▓▓▓▓▓████▓▓▓▓▓████▓▓▓▓▓████▌ ▐Ç")
    print("         ▐▌██▓▓▓▓▓████▓▀▀▀█████▓▓▓▓▓████▌  █")
    print("         █ ██▓▓▓▓█▀^████ ████░▀▀▓▓▓▓████▌  |▌")
    print("         █ ██▓▓█ ███'███ ███▀▄██▄▀█▓████▓█  █")
    print("     ,▄µ¢\████▌▄▄▓▀▀█.██▄██\▓█▀▀▄▄ █████▓▓[ █")
    print("     █ ,▄█████ ▓▓ ▄▄▓▓▓ ▄▄▓▓▓ ▄ ▓▓ ████▓▓▌ █")
    print("    ╓▀'^█████▌▓▓▓ ▓▀█▓▓ ▄▓▓▓▓ ▄ ▓▓Ü ███▓▓⌐ ▓")
    print("    █ ╓▄▓████▌▓▓▓ ▄▄█▓▓▄▄▄▓▓▓▄▄▄▓▓▓]████▓█ j▌")
    print("   ▐▌ █▓▓█████ ▓▓▓▀▀▓⌐╓▄`▀▄¬▄▓▀▓▓▓▌█████▓▌ ▐C")
    print("    ▌ █▓▓████▓█▄¢███▀╓██ ███╙████,██████▓╛ █")
    print("    ▓ └▓▓████▓▓▓█▓▀▀▄███ ████^▀▀▄▓▓▓████▌ ▓`")
    print("     █ ▐▓████▓▓▓▓▓██▄██▀,▀▀█▄█ ╣▓▓▓▓████ ▐'")
    print("      █ ╙████▓▓▓▓▓████▓ ╣╣▓████▓▓▓▓▓██▀ Æ┘")
    print("       ▀▄ ▀██▓▓▓▓▓████▓▓▓▓▓████▓▓▓▓▓█┘╓▀")
    print("         ▀▄,▀▓▓▓▓▓████▓▓▓▓▓████▓▓▓▓▀▄▀'")
    print("           ╙N▄░▀▓▓████▓▓▓▓▓████▀▀▄@▀")
    print("              '╙ªW▄▄,,▀▀▀,▄▄▄m²^")

    print("")
    print("=======================================================================================")
    print("")
    print("  #### 		 ")
    print(" ##  ## 		 ")
    print("     ##     ##")
    print("   ### 		 ")
    print("  ## 		 ")
    print(" ##  ##     ##")
    print(" ######		 ")

    print("                      ╖")
    print("                   ,,╟╫╖,")
    print("                m▓║NN╫╟N0╣╠M╕")
    print("           ╥▓▓╦▓╣╜ ,,╟▓ ,,,╝╦▓╣ÖW,")
    print("         ,▓▓╩╓▀╣▓▓▓▓▓▓B▓▓▓▓╢▓▓▄,╣▓▓")
    print("         ▓╣▓▓▓▒ ║▓▓▓▓▌╗▒▓▒▓▒,▐▓▓╣▓M╗")
    print("        ╒╜║▓▒▓▓▓▓▒▒▒▒▒▓▒▒▒▒▓▓▓▓▒▓▓╜╫")
    print("         ^╙╙▓▒▒▓█▓▒▄╢▓▓▓▓▓▒▓▓▒▒▓▓╙^")
    print("            ╙╩╣╫╗╢╢╢╣▒▒▒╢╢╢╢╣▓$▓")
    print("          ,╗╢▒╣▒╢╩╜╙^^^^╙╜╨╝╣▒▒╢@╖")
    print("        ╗╢╣▒╩▓                ▄╚╢▒▒@,")
    print("      ╗▒╣╫▀╗╢▒▒╦            ▄╢▒▒╫▄╚▒▒╫,")
    print("    ╓╣╢╫▀╣▒╣▒█▄╣▒╦╗╢╢╢╢╢╢@╦╢╣▒▀╣▒╢╢▄╝▒▒N")
    print("   ╔▒╣▓▄▒╣▒█▓▓█▒╣╣╣▒▓╜╙╟▒╣╣▒▒╫▄ ╙╣╣▒▓╙▒╣▓")
    print("  ,▒╣▓▐▒╣▓█▓█▒╣▒▓█▓▒▒▓╣▒╣╫╜'╩▒▒▓  ▓▒╣▓╙▒╣▓")
    print("  ╣╣▒j▒╣▒▀██▒╣▒█▓█▓█▓▒▒▓▌          ▓╣╣▌╢╣▒")
    print("  ▒╣▓▐╣╣▌  ▌╣▒▓█████▓██▓▓█,        ▐▒╣▒▐╣╣▌")
    print("  ▒╣▒▓╣╣▌  ▌╣▒█▓████▀▀▀▀▀█▓█▄       ▒╣▒U▒╣▌")
    print("  ▒╣▒▐▒╣▓  ▀▒╣▓ ▀▓██╣▓███▓██▓█▄    ▐▒╣▓▐╣╣▌")
    print("  ╟╣▒▌▌╣▒▄  ▓▒▒▓, ▀█╣▒▒▒▒▓█▓██▓█▄  ▒╣▒▌╣╣▒")
    print("   ╣╣▒Ω╣╣▒▄  ╙╣▒▒╢╦▓╣▓▓▓▓██▀▒╣▓▓▓█╣╣▒▌╣╣▒╛")
    print("    ╣╣▒▄╣▒▓`   `╨╣▒▒╣▒▒▒▒▒▒▄▓█▓▓█▓▒▒▀╣╣▒▀")
    print("     ╚▒▒▓▄         ▓╣▓^'╙█▓▓████▓▓▀╔╣╣╫`")
    print("       ╢▒▒╫╖       ▀╙▀    `█▓▓█▀▀╗╢╣╫╜")
    print("         ╚╣▒▒╢╦,            ▐▓@╢▒▒╩`")
    print("            ╙╝╢▒╣▒╢╢╢╢╢╢╢╢▒▒▒▒╝╜`")
    print("                 `╙╙╙╙╨╨╜╙^")

    print("")
    print("=======================================================================================")
    print("")

def imprimeTrave():
    print("")                                                                                                                                                      
    print("    *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.#                        ")
    print("    #.                                                                                        .#                        ")
    print("    #.  :*.===============================================================================#:  .#                        ")
    print("    #.  :*                                                                                *:  .#                        ")
    print("    #.  :*        1                        2  2                       3  3  3             *:  .#                        ")
    print("    #.  :*     1  1                      2      2                            3            *:  .#                        ")
    print("    #.  :*        1                           2                           3               *:  .#                        ")
    print("    #.  :*        1                        2                                 3            *:  .#                        ")
    print("    #.  :*        1                      2   2  2                     3  3  3             *:  .#                        ")
    print("    #.  :*                                                                                *:  .#                        ")
    print("    #.  :*                                                                                *:  .#                        ")
    print("    #.  :*         4                     5  5  5 5                    6   6   6           *:  .#                        ")
    print("    #.  :*      4  4                    5                            6                    *:  .#                        ")
    print("    #.  :*    4    4                     5 5 5 5                     6  6  6  6           *:  .#             _          ")
    print("    #.  :*   4  4  4 4                           5                   6         6          *:  .#          *     *       ")
    print("    #.  :*         4                     5 5 5 5                      6   6   6           *:  .#         (       )      ")
    print("    #.  :*                                                                                *:  .#          *     *       ")
    print("....#...:*................................................................................*:...#..........  ---         ")
    print("")

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    print('\nConectado')

    print('Esperando o servidor iniciar o jogo')

    start = 0
    
    while 1:
        if(start == 0):
            message = client.recv(1500)
            comandoCompletoServidor = message.decode()
            comando, hash = separaComandoComHash(comandoCompletoServidor)
            start = 100

        else:
            message = client.recv(1500)
            comandoCompletoServidor = message.decode()
            comando = separaComando(comandoCompletoServidor)

        match comando:
            case 'SELTIME':
                imprimeTimes()
                chooseTime(client)

            case 'CHTTURN':
                imprimeTrave()
                retornaATK(client)

            case 'DEFTURN':
                imprimeTrave()
                retornaDEF(client)

            case 'ATTTURN':
                atualizacaoTurno(comandoCompletoServidor, hash)

            case 'GAMEOVE':
                gameOverATT(comandoCompletoServidor, hash)
                break

            case _:
                print("COMANDO INVÁLIDO")
                break
          
main()