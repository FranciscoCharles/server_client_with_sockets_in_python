#_*_coding:utf-8_*_

'''
Copyright (c) 2021 FranciscoCharles

para informações de licenca consulte o LICENCE.txt.
'''

import socket#importa o modulo socket.

if __name__ == '__main__':#verica se este programa/arquivo é o arquivo/programa/chamada de execução principal.

    IP_SERVIDOR = 'localhost'#ip do servidor.

    with socket.socket(type = socket.SOCK_DGRAM) as servidor:#abre um socket do tipo UDP.
        servidor.bind((IP_SERVIDOR, 8080))#associa o socket ao a um IP=localhost e Porta=8081.
        print(f'servidor ativo em: {servidor.getsockname()}.')#exibe uma mensagem contendo o endereco do socket.
        mensagem = b'<servidor> resposta.'#cria uma mensagem em bytes.
        while True:#loop infinito.
            dado, endereco_cliente = servidor.recvfrom(1024)#aguarda por dados.
            if dado == b'sair':#verifica se é para sair.
                break#interrompe o loop.
            servidor.sendto(mensagem, endereco_cliente)#envia uma mensagem ao cliente.
        print('servidor inativo.')#exibe uma mensagem.
