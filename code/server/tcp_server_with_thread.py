#_*_coding:utf-8_*_

'''
Copyright (c) 2021 FranciscoCharles

para informações de licenca consulte o LICENCE.txt.
'''
import socket#importa o modulo socket.
import threading#importa o modulo threading.

def processar_conexao(conexao, endereco_alvo):#define uma funcao.
    with conexao:#enquanto a conexao nao for terminada.
        while True:#loop infinito.
            dado = conexao.recv(1024)#receba dados.
            if dado==b'sair' or not dado:#verifica se é para sair ou se não ha dados.
                conexao.shutdown(socket.SHUT_RDWR)#desligua as conexoes de envio e recebimento.
                break#interrompe o loop.
            conexao.sendall(dado)#reenvie o dado.

def criar_thread(conexao, endereco):#define uma funcao.
    thread = threading.Thread(
        target = processar_conexao,
        args = (conexao, endereco,)
    )#cria uma thread e configura seus argumentos.
    thread.start()#inicia a thread.
    return thread#retorna a thread criada.

def remover_threads_inativas(threads):#define uma funcao.
    for thread in threads:#itera as threads criadas.
        if not thread.is_alive():#verifica se a thread esta inativa.
            threads.remove(thread)#remove a thread selecionada.
    return threads#retorna lista de threads atualizada.

if __name__ == '__main__':#verica se este programa/arquivo é o arquivo/programa/chamada de execução principal.

    with socket.socket() as servidor:#abre um socket do tipo tcp.
        servidor.bind(('localhost', 8080))#associa o socket ao a um IP=localhost e Porta=8080.
        print(f'servidor ativo em: {servidor.getsockname()}.')#exibe uma mensagem contendo o endereco do socket.
        threads = []#cria uma lista vazia.
        servidor.listen()#faz o socker aceitar conexões.
        while True:#loop infinito.
            conexao, endereco_cliente = servidor.accept()#aceita uma conexao.
            thread = criar_thread(conexao, endereco_cliente)#cria uma nova thread.
            threads.append(thread)#anexa a thread recem criada.
            threads = remover_threads_inativas(threads)#remove threads inativas.