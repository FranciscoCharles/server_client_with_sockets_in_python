#_*_coding:utf-8_*_

'''
Copyright (c) 2021 FranciscoCharles

para informações de licenca consulte o LICENCE.txt.
'''
import socket#importa o modulo socket.

def processar_conexao(conexao, endereco_alvo):#define uma funcao.
    with conexao:#enquanto a conexao nao for terminada.
        while True:#loop infinito.
            dado = conexao.recv(1024)#receba dados.
            if dado==b'sair' or not dado:#verifica se é para sair ou se não ha dados.
                conexao.shutdown(socket.SHUT_RDWR)#desligua as conexoes de envio e recebimento.
                break#interrompe o loop.
            conexao.sendall(dado)#reenvie o dado.

if __name__ == '__main__':#verica se este programa/arquivo é o arquivo/programa/chamada de execução principal.

    with socket.socket() as servidor:#abre um socket do tipo tcp.
        servidor.bind(('localhost',8080))#associa o socket ao a um IP=localhost e Porta=8080.
        print(f'servidor ativo em: {servidor.getsockname()}.')#exibe uma mensagem contendo o endereco do socket.
        servidor.listen()#faz o socker aceitar conexões.
        while True:#loop infinito.
            conexao, endereco_cliente = servidor.accept()#aceita uma conexao.
            processar_conexao(conexao, endereco_cliente)#processa a conexao.