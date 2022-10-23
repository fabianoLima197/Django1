import sqlite3

def conectar():

    conn = sqlite3.connect('psqlite3.meu banco')
    conn.execute()
    print('Conectado ao servidor')
    return conn

def deconectar():


    print('desconectando do servidor')

def listar():
    print('Listando')

def inserir():
    print('Inserindo')

def atualizar():
    print('Atualizando algo')

