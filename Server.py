# Desenvolvido por: Rafael Duarte

import socket
from random import randint

clients = []
comando = []
player1 = []
player2 = []

placar1_gols = 0
placar2_gols = 0
placar1_erros = 0
placar2_erros = 0
count = 0



#Separa o nome do comando com os atributos(que variam de acordo com o comando)
def separaComando(mensagemRecebida):
    comandoSep = mensagemRecebida[0:7]
    cabecalhosSep = mensagemRecebida[7:]
    return comandoSep, cabecalhosSep

#cria e envia a mensagem para o cliente sobre a seleção de classe
def selectTime(client, hash):
    hash = int(hash)
    if(hash == 1):
        comando = 'SELTIME1'
        message = comando
        EncodMessage = message.encode()
        client.send(EncodMessage)
    else:
        comando = 'SELTIME2'
        message = comando
        EncodMessage = message.encode()
        client.send(EncodMessage)

#cria e envia a mensagem para o cliente sobre o turno de ataque
def chuteTurn(client):
    comando = 'CHTTURN'
    message = comando
    EncodMessage = message.encode()
    client.send(EncodMessage)

#cria e envia a mensagem para o cliente sobre o turno de defesa
def defTurn(client):
    comando = 'DEFTURN'
    message = comando
    EncodMessage = message.encode()
    client.send(EncodMessage)

#funcao relacionada a atualização de turno
def attTurn(clients, status_p1, status_p2, ordemATK, rodada):

    global placar1_gols
    global placar2_gols
    global placar1_erros
    global placar2_erros

    placar1_g = str(status_p1[1])
    gol_erro = str(status_p1[2])
    placar1_e = str(status_p1[3])

    p1_status_string = gol_erro + placar1_g

    print("att1: ", p1_status_string)

    placar2_g = str(status_p2[1])
    gol_erro = str(status_p2[2])
    placar2_e = str(status_p2[3])
    p2_status_string = gol_erro + placar2_g

    print("att2: ", p2_status_string)

    flag = verificaRodada(rodada)

    if(flag == 0):
        comando = 'ATTTURN'+str(ordemATK)+str(p1_status_string)+str(p2_status_string)+str(flag)
        print("Comando: ", comando) #ret
        message = comando
        EncodeMessage = message.encode()
        clients[0].send(EncodeMessage)
        clients[1].send(EncodeMessage)
        print('Enviou o comando de atualização de turno para os clients(ATTTURN)')
        flag = int(0)
        return flag
    else:
        comando = 'GAMEOVE'+str(ordemATK)+str(p1_status_string)+str(p2_status_string)+str(flag)
        message = comando
        EncodeMessage = message.encode()
        clients[0].send(EncodeMessage)
        clients[1].send(EncodeMessage)
        print('Enviou o comando de gameOver para os clients(GAMEOVE)')
        flag = int(-100)
        return flag

#funcao relacionada ao inicio do turno
def comecaTurno(client, player):

    global count

    ataque = 0
    count += 1
    print("count: ", count)
    chuteTurn(client)
    print('Enviou o comando de turno de chute para o client(CHTTURN)')
    respostaChute = client.recv(1500)
    atkDecode = respostaChute.decode()
    print('Recebeu o comando de resposta do turno de ataque do client(RETCHUT)')
    comando, direcao = separaComando(atkDecode)
    direcao = int(direcao)
    
    if(comando == 'RETCHUT' and direcao == 1):
        ataque = 1
    elif(comando == 'RETCHUT' and direcao == 2):
        ataque = 2
    elif(comando == 'RETCHUT' and direcao == 3):
        ataque = 3
    elif(comando == 'RETCHUT' and direcao == 4):
        ataque = 4
    elif(comando == 'RETCHUT' and direcao == 5):
        ataque = 5
    elif(comando == 'RETCHUT' and direcao == 6):
        ataque = 6

    return ataque

#funcao relacionada a defesa de turno
def defesaTurno(client, player):
    defesa = 0
    defTurn(client)
    print('Enviou o comando de turno de defesa para o client(DEFTURN)')
    respostaDEF = client.recv(1500)
    defDecode = respostaDEF.decode()
    print('Recebeu o comando de resposta do turno de defesa do client(DEFTURN)')
    comando, direcao = separaComando(defDecode)
    direcao = int(direcao)

    if(comando == 'DEFENDR' and direcao == 1):
        defesa = 1
    elif(comando == 'DEFENDR' and direcao == 2):
        defesa = 2
    elif(comando == 'DEFENDR' and direcao == 3):
        defesa = 3
    elif(comando == 'DEFENDR' and direcao == 4):
        defesa = 4
    elif(comando == 'DEFENDR' and direcao == 5):
        defesa = 5
    elif(comando == 'DEFENDR' and direcao == 6):
        defesa = 6
    
    return defesa

def verificaRodada(rodada):

    global placar1_gols
    global placar2_gols
    global placar1_erros
    global placar2_erros

    flagVencedor = 0
    if(rodada == 6):
        if(placar1_erros == 3 and placar2_gols > 2):
            flagVencedor = 2
        elif(placar2_erros == 3 and placar1_gols > 2):
            flagVencedor = 1
        else:
            flagVencedor = 0
    elif(rodada == 7):
        if(placar2_erros > 2 and placar1_gols > 2):
            flagVencedor = 1
        elif(placar1_erros > 2 and placar2_gols > 2):
            flagVencedor = 2
        else:
            flagVencedor = 0
    elif(rodada == 8):
        if(placar1_erros > 2 and placar2_gols > 3):
            flagVencedor = 2
        elif(placar2_erros > 2 and placar1_gols > 3):
            flagVencedor = 1
        else:
            flagVencedor = 0
    elif(rodada == 9):
        if(placar2_erros > 3 and placar1_gols > 3):
            flagVencedor = 1
        elif(placar1_erros > 3 and placar2_gols > 3):
            flagVencedor = 2
        else:
            flagVencedor = 0
    elif(rodada == 10):
        if(placar1_erros > 3 and placar2_gols > 4):
            flagVencedor = 2
        elif(placar2_erros > 3 and placar1_gols > 4):
            flagVencedor = 1
        else:
            flagVencedor = 0
    elif(rodada > 10):
        if(placar1_gols > placar2_gols):
            flagVencedor = 1
        elif(placar2_gols > placar1_gols):
            flagVencedor = 2
        elif(placar1_gols == placar2_gols):
            flagVencedor = 0
    
    return flagVencedor


#funcao realacionada aos cálculos do turno
def attPosTurno(tentativa_gol_erro, player1, player2, ordemATK, count):
    
    status_p1 = []
    status_p2 = []

    global placar1_gols
    global placar2_gols
    global placar1_erros
    global placar2_erros

    time1 = int(player1[0])
    placar1_gols = int(placar1_gols)
    placar1_erros = int(placar1_erros)

    time2 = int(player2[0])
    placar2_gols = int(placar2_gols)
    placar2_erros = int(placar2_erros)

    gol_erro = int(tentativa_gol_erro)



    status_p1.append(time1)
    status_p1.append(placar1_gols)
    status_p1.append(gol_erro)
    status_p1.append(placar1_erros)

    status_p2.append(time2)
    status_p2.append(placar2_gols)
    status_p2.append(gol_erro)
    status_p2.append(placar2_erros)

    print("attposturn aq: ", status_p1)
    print("aq: ", status_p2)

    flag = attTurn(clients, status_p1, status_p2, ordemATK, count)

    return flag


def verificaGol(chute, defesa, playerAtual, defineOrdem):
    
    global placar1_gols
    global placar2_gols
    global placar1_erros
    global placar2_erros


    gol_erro = 0

    global test_aux


    if(playerAtual[0] == 1):
        fora = randint(1, 50)
    else:
        fora = randint(1, 100)

    if(defineOrdem == 1):
        if(chute == defesa):
            print("Defesa do Goleiro!\n")
            placar1_erros += 1
            gol_erro = 0
        elif(fora <= 10):
            print("Chute para Fora!\n")
            placar1_erros += 1
            gol_erro = 1
        else:
            print("Gol!\n")
            placar1_gols += 1
            gol_erro = 2
    else:
        if(chute == defesa):
            print("Defesa do Goleiro!\n")
            placar2_erros += 1
            gol_erro = 0
        elif(fora <= 10):
            print("Chute para Fora!\n") 
            placar2_erros += 1  
            gol_erro = 1
        else:
            print("Gol!\n")
            placar2_gols += 1
            gol_erro = 2

    return gol_erro



def main():

    global count
    global placar1_gols
    global placar2_gols
    global placar1_erros
    global placar2_erros


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
        print('Server Online')
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    connectedPlayers = 0

    while True:
        if(connectedPlayers < 2):
            client, addr = server.accept()
            clients.append(client)
            print('Cliente Aceito')
            connectedPlayers += 1
        if connectedPlayers == 2:
            break
        else:
            continue
    
    #envia a requisição de selecionar time ao Player1 e recebe a resposta do mesmo
    hash = 1
    selectTime(clients[0], hash)
    print('Enviou comando pedindo Time ao Player1')
    choose_p1 = clients[0].recv(1500)
    chP1_decode = choose_p1.decode()
    print('Recebeu a resposta de Time do Player1')
    comando, p1_time = separaComando(chP1_decode)

    #envia a requisição de selecionar time ao Player2 e recebe a resposta do mesmo
    hash = 2
    selectTime(clients[1], hash)
    print('Enviou comando pedindo Time ao Player2')
    choose_p2 = clients[1].recv(1500)
    chP2_decode = choose_p2.decode()
    print('Recebeu a resposta de Time do Player2')
    comando, p2_time = separaComando(chP2_decode)

    #Add o Time do p1
    player1.append(p1_time)

    #Add o Time do p2
    player2.append(p2_time)  

    #define quem começa cabrando de forma aleatoria
    defineOrdem = randint(1, 2)
    gol_erro = 0

    while 1:
        if defineOrdem == 1:            
            print("caso1")
            valorChute_p1 = comecaTurno(clients[0], player1)
            valorDef_p2 = defesaTurno(clients[1], player2)
            ordemChute = int(1)
            gol_erro = verificaGol(valorChute_p1, valorDef_p2, player1, ordemChute)
            flagG = attPosTurno(gol_erro, player1, player2, ordemChute, count)
            if(flagG == 1):
                print('FIM DE JOGO')
                print('PLAYER 1 VENCEU')
                break
            else:
                valorChute_p2 = comecaTurno(clients[1], player2)
                valorDef_p1 = defesaTurno(clients[0],player1)
                ordemChute = int(2)
                gol_erro = verificaGol(valorChute_p2, valorDef_p1, player2, ordemChute)
                flagG = attPosTurno(gol_erro, player1, player2, ordemChute, count)
                if(flagG == 2):
                    print('FIM DE JOGO')
                    print('PLAYER 2 VENCEU')
                    break            
        else:
            print("caso2")
            valorChute_p2 = comecaTurno(clients[1], player2)
            valorDef_p1 = defesaTurno(clients[0],player1)
            ordemChute = int(2)
            gol_erro = verificaGol(valorChute_p2, valorDef_p1, player2, ordemChute)
            flagG = attPosTurno(gol_erro, player1, player2, ordemChute, count)
            if(flagG == 2):
                print('FIM DE JOGO')
                print('PLAYER 2 VENCEU')
                break
            else:
                valorChute_p1 = comecaTurno(clients[0], player1)
                valorDef_p2 = defesaTurno(clients[1],player2)
                ordemChute = int(1)
                gol_erro = verificaGol(valorChute_p1, valorDef_p2, player1, ordemChute)
                flagG = attPosTurno(gol_erro, player1, player2, ordemChute, count)
                if(flagG == 1):
                    print('FIM DE JOGO')
                    print('PLAYER 1 VENCEU')
                    break
                
main()