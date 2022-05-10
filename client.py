# Joálisson Clemente \\ Adaylton Silva
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 7777))

print('Conectado!!\n')


while True:
    print("-------- COTAÇÃO DE MOEDAS --------")
    print("1 - Cotação do Dólar")
    print("2 - Cotação do Euro")
    print("3 - Cotação do Bitcoins")
    print("0 - Não desejo mais utilizar os serviços")

    opt = int(input("Digite a opção que deseja: "))

    
    if (opt == 1):
        client.send(b'1')
        cotacao = client.recv(1024).decode()
        print(cotacao)
    
    elif (opt == 2):
        client.send(b'2')
        cotacao = client.recv(1024).decode()
        print(cotacao)

    elif (opt == 3):
        client.send(b'3')
        cotacao = client.recv(1024).decode()
        print(cotacao)
        
    if(opt == 0):
        print("Conexão encerrada!!!")
        break