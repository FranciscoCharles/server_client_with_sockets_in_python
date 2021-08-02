#_*_coding:utf-8_*_

'''
Copyright (c) 2021 FranciscoCharles

para informações de licenca consulte o LICENCE.txt.
'''
import time#importa o modulo time.
import socket#importa o modulo socket.
import numpy#importa o modulo numpy

def ping(sock, ip_alvo, porta_alvo = 8080, n_repeticoes = 10):#define uma funcao.
    
    intervalos = numpy.zeros((n_repeticoes))#cria um  array de zeros de intervalos.
    mensagem = b'<cliente>: mensagem.'#cria uma mensagem em bytes.
    endereco_alvo = (ip_alvo,porta_alvo)#cria uma tupla com o endereco alvo.

    for index in range(n_repeticoes+1):#itera n_repeticoes+1 vezes.
        try:

            if index == n_repeticoes:#verifica se é a ultima iteracao.
                mensagem = b'sair'#troca a mensagem
            sock.sendto(mensagem, endereco_alvo)#envia a mensagem ao endereco alvo.
            
            if mensagem != b'sair':#verifica se não é para sair.
                t0 = time.perf_counter()#regista o segundos atuais.
                sock.recvfrom(1024)#aguarda por dados.
                intervalo = (time.perf_counter()-t0)*1000#calcula os segundos decorritos e converte para milisegundos.
                print(f'ping:{index:2d} tempo decorrido: {intervalo:.2f}ms')#exibe o ping atual e o intervalo decorrido.
                intervalos[index] = intervalo#armazena o intervalo.

        except socket.timeout:#captura a excecao de timeout.
            print('Erro: ops, tempo esgotado...')#exibe uma mensagem.
    #exibe as informacoes referentes aos intervalos em milisegundos.
    print(f'informacoes de intervalo:')
    print(f'\tmedio: {intervalos.mean():.2f}ms')
    print(f'\tdevio padrao: {intervalos.std():.2f}ms')
    print(f'\tmaximo: {intervalos.max():.2f}ms')
    print(f'\tminimo: {intervalos.min():.2f}ms')

if __name__ == '__main__':#verica se este programa/arquivo é o arquivo/programa/chamada de execução principal.

    IP_SERVIDOR = 'localhost'#ip do servidor.

    with socket.socket() as cliente:#abre um soket do tipo TCP.
        cliente.settimeout(10)#seta o timeout em 10s.
        try:
            cliente.connect((IP_SERVIDOR, 8080))#tenta se conectar ao servidor na porta 8080.
            ping(cliente,IP_SERVIDOR)#realiza os pings.
        except ConnectionRefusedError:#captura a excecao.
            print('Erro: ops, parece que a conexao foi recusada.')#exibe uma mensagem.