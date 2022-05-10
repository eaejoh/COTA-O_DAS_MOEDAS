import socket
import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL'] ['bid']
cotacao_euro = cotacoes['EURBRL'] ['bid']
cotacao_bitcoins= cotacoes['BTCBRL'] ['bid']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
server.listen(10)
print('......Aguardando conexão...... \n')

connection, address = server.accept()
print('.............................')
print('Conexão aceita!!!\n')

while True:
    namefile = connection.recv(1024).decode()
    print(namefile)

    if namefile == '1':
        connection.send(bytearray(cotacao_dolar, 'utf-8'))

    if namefile == '2':
        connection.send(bytearray(cotacao_euro, 'utf-8'))

    if namefile == '3':
        connection.send(bytearray(cotacao_bitcoins, 'utf-8'))

    if namefile == '0':
        connection.send(bytearray(cotacao_bitcoins, 'utf-8'))
       
        break
connection.close()